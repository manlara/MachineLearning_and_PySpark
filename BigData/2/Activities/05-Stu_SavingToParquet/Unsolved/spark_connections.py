
# Postgres
def postgresUrlProperties(connection):
    # Postgres credentials
    jdbcHostname = connection['host']
    jdbcPort = connection['port']
    jdbcDatabase = connection['database']
    dialect = connection['dialect']
    jdbcUsername = connection['username']
    jdbcPassword = connection['password']
    
    jdbcUrl = f"jdbc:{dialect}://{jdbcHostname}:{jdbcPort}/{jdbcDatabase}"
    # for mysql driver = com.mysql.jdbc.Driver
    connectionProperties = {
      "user" : jdbcUsername,
      "password" : jdbcPassword,
      "driver" : "org.postgresql.Driver" 
    }
    return (jdbcUrl, connectionProperties)

# Mongo credentials
def createMongoURI(connection, database, collection):
    mongoHostname = connection['hostname']
    mongoPort = connection['port']
    mongoDatabase = database
    mongoCollection = collection
    mongoUsername = connection.get('username')
    mongoPassword = connection.get('password')
    mongoReplica = connection.get('replica')
    
    baseURI = "mongodb://"
    if bool(mongoUsername) and bool(mongoPassword):
        baseURI += f"{mongoUsername}:{mongoPassword}@"
    mongoHosts = ",".join([
        f"{host}:{mongoPort}"
        for host in mongoHostname.split(",")
    ])
    mongoURI = f"{baseURI}{mongoHosts}/{mongoDatabase}"
    if bool(mongoReplica):
        mongoURI = f"{mongoURI}.{mongoCollection}?replicaSet={mongoReplica}"
    else:
        mongoURI = f"{mongoURI}.{mongoCollection}"
    return mongoURI


