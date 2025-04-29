import pandas as pd
import os

def load_and_prepare_data():
    """
    Loads the SOUTHSOUTH.csv dataset and recodes relevant variables.

    Returns:
        pd.DataFrame: Cleaned and preprocessed DataFrame
    """
    # Dynamically locate the file within the project structure
    data_path = os.path.join(os.path.dirname(__file__), "data", "SOUTHSOUTH.csv")
    df = pd.read_csv(data_path)

    # Recode SES
    df['SES_Label'] = df['ASDHSES'].replace({
        3.0: 'Lower', 2.0: 'Middle', 1.0: 'Higher'
    })

    # Recode Reading Attitude
    df['ReadAtt_Label'] = df['ASDGSLR'].replace({
        3.0: 'Do Not Like', 2.0: 'Somewhat Like', 1.0: 'Very Much Like'
    })

    # Recode Parental Involvement
    df['ParentalInv_Collapsed'] = df['ACBG11F'].replace({
        1.0: 'High', 2.0: 'High', 3.0: 'Medium', 4.0: 'Low', 5.0: 'Low'
    })

    # Convert to ordered categories
    df['SES_Label'] = pd.Categorical(df['SES_Label'], categories=['Lower', 'Middle', 'Higher'], ordered=True)
    df['ParentalInv_Collapsed'] = pd.Categorical(df['ParentalInv_Collapsed'], categories=['Low', 'Medium', 'High'], ordered=True)
    df['ReadAtt_Label'] = pd.Categorical(df['ReadAtt_Label'], categories=['Do Not Like', 'Somewhat Like', 'Very Much Like'], ordered=True)

    # Subset relevant columns
    df = df[['SES_Label', 'ParentalInv_Collapsed', 'ReadAtt_Label', 'ASRREA01']]
    df = df.dropna()

    return df
