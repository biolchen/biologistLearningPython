read_from_sql <- function(a_table, a_dbFile) {
  require(DBI)
  require(RSQLite)
  con <- dbConnect(SQLite(), a_dbFile)
  query <- glue('select * from {a_table};')
  df <- dbGetQuery(con, query)
  dbDisconnect(con)
  return(df)
}