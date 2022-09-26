import pandas as pd


class FileLoader:
    def load(self, path: str) -> pd.DataFrame | None:
        try:
            if not isinstance(path, str):
                raise TypeError
            df = pd.read_csv(path)
            print(f'Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}')
            return df
        except (FileNotFoundError, TypeError) as e:
            print(f'ERROR. {e}')
            return None

    def display(self, df: pd.DataFrame, n: int) -> None:
        if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
            print('ERROR. Giving wrong values to Fileloader.display')
            return
        if n < 0:
            print(df.tail(-n))
        else:
            print(df.head(n))
