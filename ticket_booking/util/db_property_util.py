class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file_name):
        try:
            with open(property_file_name, 'r') as file:
                properties = {}
                for line in file:
                    key, value = line.strip().split('=')
                    properties[key.strip()] = value.strip()

                
                db_url = properties.get('db_url')
                db_user = properties.get('db_user')
                db_password = properties.get('db_password')

                if db_url and db_user and db_password:
                    return f"jdbc:{db_url}?user={db_user}&password={db_password}"
                else:
                    raise Exception("Incomplete database properties in the file.")
        except Exception as e:
            print(f"Error in get_connection_string: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    property_file_name = "db.properties"  # Change this to your actual properties file
    connection_string = DBPropertyUtil.get_connection_string(property_file_name)

    if connection_string:
        print(f"Connection String: {connection_string}")
    else:
        print("Failed to retrieve connection string.")
