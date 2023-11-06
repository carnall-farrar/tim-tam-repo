from dotenv import load_dotenv
import pandas as pd
import os
from pyathena import connect
from pyathena.async_cursor import AsyncCursor
from pyathena.cursor import DictCursor
from pyathena.pandas.util import as_pandas


class AthenaQueryPandas:
    """Convenient abstraction of AWS Athena connection, for querying data and receiving pandas DataFrame results"""

    def _load_vars(self):
        load_dotenv()
        self.aws_access_key = os.getenv("AWS_ACCESS_KEY")
        self.aws_secret_key = os.getenv("AWS_SECRET_KEY")
        self.aws_athena_s3_staging_dir = os.getenv("AWS_ATHENA_S3_STAGING_DIR")
        self.aws_region = os.getenv("AWS_REGION")
        self.aws_athena_schema_name = os.getenv("AWS_ATHENA_SCHEMA_NAME")

    def _make_cursor(self, is_async: bool = False):
        args = dict(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
            s3_staging_dir=self.aws_athena_s3_staging_dir,
            region_name=self.aws_region,
        )
        if is_async:
            cursor = connect(
                **args,
                cursor_class=AsyncCursor,
            ).cursor()
        else:
            cursor = connect(**args).cursor(DictCursor)
        return cursor

    def __init__(self) -> None:
        self._load_vars()
        self.cursor = self._make_cursor(False)

    def query(self, query: str) -> pd.DataFrame:
        """Query HES tables via Athena connection"""
        self.cursor.execute(query)
        return as_pandas(self.cursor)


def test_query():
    test_query = """
    SELECT 
        epikey,
        token_person_id
    FROM 
        "vitalstatistix-lambda"."hes"."ecds_preview" 
    limit 10;
    """
    ac = AthenaQueryPandas()
    result: pd.DataFrame = ac.query(test_query)
    print(result)
    assert result.shape == (10, 2)


if __name__ == "__main__":
    test_query()
    print("End athena test")
