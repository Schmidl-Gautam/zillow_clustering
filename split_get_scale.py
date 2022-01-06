from prepare import Prepare
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class SplitGetScale:

    def split(self, df):

        train, test = train_test_split(df, test_size=.15, random_state=123)
        train, validate = train_test_split(train, test_size=.2, random_state=123)

        return train, validate, test

    # COLUMNS NEED TO BE UPDATE BEFORE MODELING
    # def get_Xy(self, train, validate, test):

    #     X_train = train.drop(["home_tax_value", "fips", "year_built", "county"], axis=1)
    #     y_train = train["home_tax_value"]

    #     X_val = validate.drop(["home_tax_value", "fips", "year_built", "county"], axis=1)
    #     y_val = validate["home_tax_value"]

    #     X_test = test.drop(["home_tax_value", "fips", "year_built", "county"], axis=1)
    #     y_test = test["home_tax_value"]

    #     return (X_train, y_train), (X_val, y_val), (X_test, y_test)

    # UPDATE COLUMNS IN GET_XY BEFORE USING THIS
    # def scale(self, X_train, X_validate, X_test):

    #     scale = StandardScaler()
    #     scale.fit(X_train)

    #     X_train_scaled = pd.DataFrame(data=scale.transform(X_train), columns=X_train.columns)
    #     X_val_scaled = pd.DataFrame(data=scale.transform(X_validate), columns=X_train.columns)
    #     X_test_scaled = pd.DataFrame(data=scale.transform(X_test), columns=X_train.columns)

    #     return X_train_scaled, X_val_scaled, X_test_scaled, scale