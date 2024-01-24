import pandas as pd
from sklearn.preprocessing import LabelEncoder


def correlation(file_path: str):
    """
    Load the CSV file into a pandas DataFrame,
    and calculate the correlation coefficients
    between 'knight' and other columns.

    Arguments:
        file_path: The path to the CSV file.
    Returns:
        None
    """
    try:
        df = pd.read_csv(file_path)

        # Use label encoding for the 'knight' column
        label_encoder = LabelEncoder()
        df['knight'] = label_encoder.fit_transform(df['knight'])

        # Calculate the correlation coefficients between 'knight' and other columns
        correlation_with_target = df.corr()['knight'].abs().sort_values(ascending=False)

        # Display the sorted correlation coefficients
        print(correlation_with_target)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main():
    correlation('../ex00/Train_knight.csv')


if __name__ == '__main__':
    main()
