#!/usr/bin/python
import codecs
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF

target=[
'http://en.wikipedia.org/wiki/A.C._Crispin',
]

#this opens a text file, using codecs so it can print non-standard characters
f = codecs.open("dbbio.txt", encoding='utf-8', mode='w+')
for item in target:
# this uses the sparqlwrapper and a sparql query that asks for each page in the
#list above to get the following rdf elements, if they exist
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        SELECT * WHERE {
        SELECT ?label ?homepage ?wikisite ?activeYearsEndYear ?activeYearsStartYear ?birthDate ?birthName ?birthPlace ?deathDate ?education ?ethnicity ?genre ?influenced ?influencedBy ?movement ?occupation ?notableWork ?spouse ?wikiPageID ?alternativeNames ?debutWorks ?nationality ?notableWorks ?period ?placeofBirth ?placeofDeath ?title ?subject ?comment ?sameAs ?depiction
        
        WHERE {
              ?writer foaf:isPrimaryTopicOf <""" +item+ """>
              
            OPTIONAL { ?writer rdfs:label ?label }
            OPTIONAL { ?writer foaf:homepage ?homepage }
            OPTIONAL { ?writer foaf:isPrimaryTopicOf ?wikisite }
            OPTIONAL { ?writer dbpedia-owl:activeYearsEndYear ?activeYearsEndYear }
            OPTIONAL { ?writer dbpedia-owl:activeYearsStartYear ?activeYearsStartYear }
            OPTIONAL { ?writer dbpedia-owl:birthDate ?birthDate }
            OPTIONAL { ?writer dbpedia-owl:birthName ?birthName }
            OPTIONAL { ?writer dbpedia-owl:birthPlace ?birthPlace }
            OPTIONAL { ?writer dbpedia-owl:deathDate ?deathDate }
            OPTIONAL { ?writer dbpedia-owl:education ?education }
            OPTIONAL { ?writer dbpedia-owl:ethnicity ?ethnicity }
            OPTIONAL { ?writer dbpedia-owl:genre ?genre }
            OPTIONAL { ?writer dbpedia-owl:influenced ?influenced }
            OPTIONAL { ?writer dbpedia-owl:influencedBy ?influencedBy }
            OPTIONAL { ?writer dbpedia-owl:movement ?movement }
            OPTIONAL { ?writer dbpedia-owl:occupation ?occupation }
            OPTIONAL { ?writer dbpedia-owl:notableWork ?notableWork }
            OPTIONAL { ?writer dbpedia-owl:spouse ?spouse }
            OPTIONAL { ?writer dbpedia-owl:wikiPageID ?wikiPageID }
            OPTIONAL { ?writer dbpedia2:debutWorks ?debutWorks }
            OPTIONAL { ?writer dbpedia2:nationality ?nationality }
            OPTIONAL { ?writer dbpedia2:notableWorks ?notableWorks }              OPTIONAL { ?writer dbpedia2:period ?period }
            OPTIONAL { ?writer dbpedia2:title ?title }
            OPTIONAL { ?writer dcterms:subject ?subject }
            OPTIONAL { ?writer rdfs:comment ?comment }
            OPTIONAL { ?writer dcterms:subject ?subject }
            OPTIONAL { ?writer owl:sameAs ?sameAs }
            OPTIONAL { ?writer foaf:depiction ?depiction }

        FILTER (LANGMATCHES(LANG(?label), 'en'))

        }
        }    
        LIMIT 1
        """)

 #  this sets the return format and converts it to a dictionary 
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        try:
            label=result["label"]["value"]
            homepage=result["homepage"]["value"]
            wikisite=result["wikisite"]["value"]
            activeYearsEndYear=result["activeYearsEndYear"]["value"]
            activeYearsStartYear=result["activeYearsStartYear"]["value"]
            birthDate=result["birthDate"]["value"]
            birthName=result["birthName"]["value"]
            birthPlace=result["birthPlace"]["value"]
            deathDate=result["deathDate"]["value"]
            education=result["education"]["value"]
            ethnicity=result["ethnicity"]["value"]
            genre=result["genre"]["value"]
            influenced=result["influenced"]["value"]
            influencedBy=result["influencedBy"]["value"]
            movement=result["movement"]["value"]
            occupation=result["occupation"]["value"]
            notableWork=result["notableWork"]["value"]
            spouse=result["spouse"]["value"]
            wikiPageID=result["wikiPageID"]["value"]
            alternativeNames=result["alternativeNames"]["value"]
            debutWorks=result["debutWorks"]["value"]
            nationality=result["nationality"]["value"]
            notableWorks=result["notableWorks"]["value"]
            period=result["period"]["value"]
            placeofBirth=result["placeofBirth"]["value"]
            placeofDeath=result["placeofDeath"]["value"]
            title=result["title"]["value"]
            subject=result["subject"]["value"]
            comment=result["comment"]["value"]
            sameAs=result["sameAs"]["value"]
            depiction=result["depiction"]["value"]
    

            #then each value is written in a row, except when there is an error 
        
            row=label+","+homepage+","+wikisite+","+activeYearsEndYear+","+activeYearsStartYear+","
            +birthDate+","+birthName+","+birhtPlace+","+deathDate+","+education+","+ethnicity+","
            +genre+","+influenced+","+influencedBy+","+movement+","+occupation+","+notableWork+","
            +spouse+","+wikiPageID+","+alternativeNames+","+debutWorks+","+nationality+","
            +notableWorks+","+period+","+placeOfBirth+","+placeofDeath+","+title+","+subject+","
            +comment+","+sameAs+","+depiction+"\n"

            f.write(row)
        except:
            pass
    
