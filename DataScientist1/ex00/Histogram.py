import pandas as pd
import matplotlib.pyplot as plt


def first_histogram():
    """
    Load the CSV file into a pandas DataFrame,
    and create a histogram for each column.

    Arguments:
        None
    Returns:
        None
    """
    try:
        file_path = 'Test_knight.csv'
        df = pd.read_csv(file_path)

        columns = df.columns

        fig, axes = plt.subplots(nrows=6, ncols=5, figsize=(15, 15),
                                 tight_layout=True)

        axes = axes.flatten()

        for i, column in enumerate(columns):
            ax = axes[i]
            ax.hist(df[column], bins=50, color='limegreen', edgecolor='none')
            ax.set_title(column)
            ax.set_xlabel('Values')
            ax.set_ylabel('Frequency')
            ax.legend(['Knight'], loc='upper right')

        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def second_histogram():
    """
    Load the CSV file into a pandas DataFrame,
    and create a histogram for each column
    depending on the type of knight.

    Arguments:
        None
    Returns:
        None
    """
    try:
        file_path = 'Train_knight.csv'
        df = pd.read_csv(file_path)

        columns = df.columns[:-1]

        fig, axes = plt.subplots(6, 5, figsize=(15, 15), tight_layout=True)

        axes = axes.flatten()

        for i, column in enumerate(columns):
            ax = axes[i]

            jedi_data = df[df['knight'] == 'Jedi'][column]
            sith_data = df[df['knight'] == 'Sith'][column]

            ax.hist(jedi_data, bins=50, color='blue', alpha=0.4,
                    edgecolor='none', label='Jedi')
            ax.hist(sith_data, bins=50, color='red', alpha=0.4,
                    edgecolor='none', label='Sith')

            ax.set_title(column)
            ax.set_xlabel('Values')
            ax.set_ylabel('Frequency')

            ax.legend(loc='upper right')

        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main():
    """
    Main function
    """
    first_histogram()
    second_histogram()


if __name__ == "__main__":
    main()
