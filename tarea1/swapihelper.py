import requests
import json

def get_movies():
    query = { "query":
    '''
    {
      allFilms {
        edges {
          node {
            id
            title
            director
            producers
            episodeID
            releaseDate
          }
        }
      }
    }
    '''}
    initial_data = json.loads(requests.get('https://swapi-graphql-integracion-t3.herokuapp.com', query).text)["data"]['allFilms']['edges']
    params = ["title", "releaseDate", "director", "producers", "episodeID", "id"]
    processed_data = sorted([{param : film["node"][param] for param in params} for film in initial_data], key=lambda x: x["episodeID"])
    for pos in range(len(processed_data)):
        processed_data[pos]["producers"] = ", ".join(processed_data[pos]["producers"])
    return processed_data


def get_movie(id):
    query = { "query":
    '''
    {
    film(id: \"0\") {
        id
        episodeID
        title
        openingCrawl
        releaseDate
        director
        producers
        characterConnection {
          characters {
            name
            id
          }
        }
        starshipConnection {
          starships {
            name
            id
          }
        }
        planetConnection {
          planets {
            name
            id
          }
        }
      }
    }
    '''.replace("0",id)}
    initial_data = json.loads(requests.get('https://swapi-graphql-integracion-t3.herokuapp.com', query).text)["data"]["film"]
    params = ["title", "releaseDate", "director", "producers", "episodeID", "id",
    "openingCrawl"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data["producers"] = ", ".join(processed_data["producers"])
    processed_data["characters"] = initial_data["characterConnection"]["characters"]
    processed_data["planets"] = initial_data["planetConnection"]["planets"]
    processed_data["starships"] = initial_data["starshipConnection"]["starships"]
    return processed_data


def get_character(id):

    query = { "query":
    '''
    {
      person(id: \"0\") {
        name
        height
        mass
        hairColor
        skinColor
        eyeColor
        birthYear
        gender
        homeworld{
            id
            name
        }
        filmConnection{
            films{
                title
                id
            }
        }
        starshipConnection{
            starships{
                name
                id
            }
        }
      }
    }
    '''.replace("0",id)}
    initial_data = json.loads(requests.get('https://swapi-graphql-integracion-t3.herokuapp.com', query).text)["data"]["person"]
    params = ["name", "height", "mass", "hairColor", "skinColor", "eyeColor",
    "birthYear", "gender", "homeworld"]
    obj_params = ["films", "starships"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data["films"] = initial_data["filmConnection"]["films"]
    processed_data["starships"] = initial_data["starshipConnection"]["starships"]
    return processed_data

def get_planet(id):
    query = { "query":
    '''
    {
      planet(id: \"0\") {
        name
        rotationPeriod
        orbitalPeriod
        diameter
        climates
        gravity
        terrains
        surfaceWater
        population
        filmConnection{
            films{
                title
                id
            }
        }
        residentConnection{
            residents{
                name
                id
            }
        }
      }
    }
    '''.replace("0", id)}
    initial_data = json.loads(requests.get('https://swapi-graphql-integracion-t3.herokuapp.com', query).text)["data"]["planet"]
    params = ["name", "rotationPeriod", "orbitalPeriod", "diameter", "climates", "gravity",
    "terrains", "surfaceWater", "population"]
    obj_params = ["films", "residents"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data["films"] = initial_data["filmConnection"]["films"]
    processed_data["residents"] = initial_data["residentConnection"]["residents"]
    processed_data["terrains"] = ", ".join(processed_data["terrains"])
    processed_data["climates"] = ", ".join(processed_data["climates"])
    return processed_data

def get_starship(id):
    query = { "query":
    '''
    {
      starship(id: \"0\") {
        name
        model
        manufacturers
        costInCredits
        length
        maxAtmospheringSpeed
        crew
        passengers
        cargoCapacity
        consumables
        hyperdriveRating
        MGLT
        starshipClass
        filmConnection{
            films{
                title
                id
            }
        }
        pilotConnection{
            pilots{
                name
                id
            }
        }
      }
    }
    '''.replace("0", id)}
    initial_data = json.loads(requests.get('https://swapi-graphql-integracion-t3.herokuapp.com', query).text)["data"]["starship"]
    params = ["name", "model", "manufacturers", "costInCredits", "length", "maxAtmospheringSpeed",
    "crew", "passengers", "cargoCapacity", "consumables", "hyperdriveRating",
    "MGLT", "starshipClass"]
    processed_data = {param : initial_data[param] for param in params}
    processed_data["pilots"] = initial_data["pilotConnection"]["pilots"]
    processed_data["films"] = initial_data["filmConnection"]["films"]
    processed_data["manufacturers"] = ", ".join(processed_data["manufacturers"])

    return processed_data
