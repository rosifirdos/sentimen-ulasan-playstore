import argparse
from datetime import datetime
from pathlib import Path

import pandas as pd
from google_play_scraper import Sort, reviews


def fetch_reviews(app_id: str, lang: str, country: str, count: int) -> pd.DataFrame:
    """Fetch up to `count` reviews for a single app."""
    rows = []
    token = None

    while len(rows) < count:
        batch_size = min(200, count - len(rows))
        result, token = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=Sort.NEWEST,
            count=batch_size,
            continuation_token=token,
        )
        if not result:
            break
        rows.extend(result)
        if token is None:
            break

    frame = pd.DataFrame(rows)
    frame["app_id"] = app_id
    return frame


def clean_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Keep relevant columns and remove empty/duplicate content."""
    selected_columns = [
        "app_id",
        "reviewId",
        "userName",
        "score",
        "at",
        "content",
        "thumbsUpCount",
        "replyContent",
        "repliedAt",
    ]
    available_columns = [col for col in selected_columns if col in df.columns]
    cleaned = df[available_columns].copy()
    cleaned["content"] = cleaned["content"].astype(str).str.strip()
    cleaned = cleaned[cleaned["content"].str.len() > 3]
    cleaned = cleaned.drop_duplicates(subset=["content"])
    cleaned = cleaned.reset_index(drop=True)
    return cleaned


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape Play Store reviews.")
    parser.add_argument("--target", type=int, default=4500, help="Target total rows")
    parser.add_argument("--lang", type=str, default="id", help="Review language")
    parser.add_argument("--country", type=str, default="id", help="Review country")
    parser.add_argument(
        "--app-id",
        type=str,
        default="com.tokopedia.tkpd",
        help="Play Store app id to scrape",
    )
    args = parser.parse_args()

    print(f"Scraping {args.app_id}...")
    all_reviews = fetch_reviews(
        app_id=args.app_id,
        lang=args.lang,
        country=args.country,
        count=args.target,
    )
    print(f"Retrieved {len(all_reviews)} rows")
    cleaned_reviews = clean_frame(all_reviews)

    if len(cleaned_reviews) < 3000:
        raise RuntimeError(
            f"Rows after cleaning is {len(cleaned_reviews)}. "
            "Please increase --target or add more apps."
        )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cleaned_reviews["scraped_at"] = timestamp

    output_dir = Path("dataset")
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_path = output_dir / "playstore_reviews_raw.csv"
    cleaned_reviews.to_csv(raw_path, index=False, encoding="utf-8")

    print(f"Saved {len(cleaned_reviews)} rows to {raw_path}")


if __name__ == "__main__":
    main()
