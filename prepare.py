from acquire import Acquire
import numpy as np

# SOME OF THIS CODE WAS BORROWED FROM CLASS REVIEW

class Prepare:

    @classmethod
    def __get_single_unit(cls):

        df = Acquire().get_zillow_data()

        single_use = [261, 262, 263, 264, 266, 268, 273, 276, 279]
        df = df[df["propertylandusetypeid"].isin(single_use)]
        df = df[(df["bedroomcnt"] > 0) & (df["bathroomcnt"] > 0) & ((df["unitcnt"] <= 1) | df["unitcnt"].isnull()) & (df["calculatedfinishedsquarefeet"] > 350)]

        return df

    @classmethod
    def __remove_missing_values(cls, prop_required_column=.70, prop_required_row=.70):

        df = Prepare.__get_single_unit()
        threshold = int(prop_required_column*len(df))
        df.dropna(axis=1, thresh=threshold, inplace=True)
        threshold = int(prop_required_row*len(df.columns))
        df.dropna(axis=0, thresh=threshold, inplace=True)

        return df

    @classmethod
    def __fill_zillow(cls):

        df = Prepare.__remove_missing_values()
        df["lotsizesquarefeet"].fillna(7313, inplace=True)

        return df

    @classmethod
    def __dropping_cols(cls):

        df = Prepare.__fill_zillow()

        cols_drop = ['id','calculatedbathnbr', 'fullbathcnt', 'propertycountylandusecode', 'propertylandusetypeid', "propertylandusedesc", "finishedsquarefeet12"]
        df.drop(columns=cols_drop, inplace=True)

        return df

    def wrangle_zillow(self):

        df = Prepare.__dropping_cols()

        df = df[(df["taxvaluedollarcnt"] < 5000000) & (df["calculatedfinishedsquarefeet"] < 8000)]

        condlist = [df["fips"] == 6037.0, df["fips"] == 6059.0, df["fips"] == 6111.0]
        choicelist = ["Los Angeles", "Orange", "Ventura"]
        df["county"] = np.select(condlist, choicelist)

        df.dropna(inplace=True)

        # rename columns for reability
        cols_rename = {"parcelid": "parcel_id", "bedroomcnt": "bedrooms", "bathroomcnt": "bathrooms", "calculatedfinishedsquarefeet": "square_feet", "taxvaluedollarcnt": "home_tax_value", "yearbuilt": "year_built"}
        zillow.rename(cols_rename, axis=1, inplace=True)

        return df