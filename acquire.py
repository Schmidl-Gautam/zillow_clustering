import pandas as pd
from env import username, password, hostname

class Acquire:

    @classmethod
    def __get_connection(cls, db, user=username, password=password, host=hostname):
            """get_connection: connects to mysql database

            Args:
                db (string): db to connect
                user (string, optional): name of user with which to login. Defaults to un.
                password (string, optional): password of user with which to login. Defaults to pw.
                host (string, optional): host name to connect. Defaults to hn.

            Returns:
                [string]: [string used to connect to mysql]
            """
            return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    def get_zillow_data(self):
            """__get_zillow_data: get data from csv or mysql

            Returns:
                pandas dataframe: used for analysis and modeling
            """
            filename = "zillow.csv"
            db = "zillow"

            try:
                df = pd.read_csv(filename)

            except:
                print(f"{filename} not found. Connecting to MySQL database and reading table to dataframe.")

                # read the SQL query into a dataframe
                query = """SELECT prop.*,
                                    pred.logerror,
                                    pred.transactiondate,
                                    air.airconditioningdesc,
                                    arch.architecturalstyledesc,
                                    build.buildingclassdesc,
                                    heat.heatingorsystemdesc,
                                    landuse.propertylandusedesc,
                                    story.storydesc,
                                    construct.typeconstructiondesc
                            FROM properties_2017 prop
                            INNER JOIN (SELECT parcelid,
                                                logerror,
                                                Max(transactiondate) transactiondate
                                        FROM predictions_2017
                                        GROUP BY parcelid, logerror) pred
                            USING (parcelid)
                            LEFT JOIN airconditioningtype air USING (airconditioningtypeid)
                            LEFT JOIN architecturalstyletype arch USING (architecturalstyletypeid)
                            LEFT JOIN buildingclasstype build USING (buildingclasstypeid)
                            LEFT JOIN heatingorsystemtype heat USING (heatingorsystemtypeid)
                            LEFT JOIN propertylandusetype landuse USING (propertylandusetypeid)
                            LEFT JOIN storytype story USING (storytypeid)
                            LEFT JOIN typeconstructiontype construct USING (typeconstructiontypeid)
                            WHERE transactiondate LIKE "2017%" and prop.latitude IS NOT NULL AND prop.longitude IS NOT NULL;
                            """
                df = pd.read_sql(query, Acquire.__get_connection(db))
                print("Connected successfully")

                # Cache the data for later
                df.to_csv(filename, index=False)
                print(f"Table saved to {filename}")

            finally:
                return df