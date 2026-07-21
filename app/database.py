from sqlalchemy import create_engine, text

from .config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def insert_books(books_data):
    if not books_data:
        return

    with engine.connect() as conn:
        for book in books_data:
            conn.execute(
                text(
                    """
                    INSERT INTO books (
                        id,
                        title,
                        price,
                        rating,
                        stock,
                        detail_page,
                        description,
                        upc,
                        product_type,
                        price_excluded_tax,
                        price_included_tax,
                        tax,
                        availability,
                        reviews
                    )
                    VALUES (
                        :id,
                        :title,
                        :price,
                        :rating,
                        :stock,
                        :detail_page,
                        :description,
                        :upc,
                        :product_type,
                        :price_excluded_tax,
                        :price_included_tax,
                        :tax,
                        :availability,
                        :reviews
                    )
                    ON CONFLICT (id) DO NOTHING
                    """
                ),
                book,
            )
        conn.commit()

    print("Data saved successfully!")