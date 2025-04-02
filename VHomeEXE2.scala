// Neo4jConnector.scala
import org.neo4j.driver._

object Neo4jConnector {
  def connect(uri: String, user: String, password: String): Session = {
    val driver: Driver = GraphDatabase.driver(uri, AuthTokens.basic(user, password))
    driver.session()
  }
}
