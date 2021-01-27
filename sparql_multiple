import csv
import codecs
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF

target=[
'http://en.wikipedia.org/wiki/A.C._Crispin',
'http://en.wikipedia.org/wiki/Ann_Bridge',
'http://en.wikipedia.org/wiki/Anne_Rice',
'http://en.wikipedia.org/wiki/B._M._Bower',
'http://en.wikipedia.org/wiki/Barry_N._Malzberg',
'http://en.wikipedia.org/wiki/C._L._Moore',
'http://en.wikipedia.org/wiki/Charlotte_Riddell',
'http://en.wikipedia.org/wiki/Chelsea_Quinn_Yarbro',
'http://en.wikipedia.org/wiki/Cyril_M._Kornbluth',
'http://en.wikipedia.org/wiki/Doris_May_Lessing',
'http://en.wikipedia.org/wiki/Dorothy_Heydt',
'http://en.wikipedia.org/wiki/Dorothy_J._Heydt',
'http://en.wikipedia.org/wiki/Eluki_bes_shahar',
'http://en.wikipedia.org/wiki/Emma_Tennant',
'http://en.wikipedia.org/wiki/George_Eliot',
'http://en.wikipedia.org/wiki/Gertrude_Barrows_Bennett',
'http://en.wikipedia.org/wiki/Gilles_Thomas',
'http://en.wikipedia.org/wiki/Harriet_Adams',
'http://en.wikipedia.org/wiki/Isak_Dinesen',
'http://en.wikipedia.org/wiki/James_Tiptree,_Jr.',
'http://en.wikipedia.org/wiki/Jayge_Carr',
'http://en.wikipedia.org/wiki/Jean_Marie_Stine',
'http://en.wikipedia.org/wiki/Jennifer_Roberson',
'http://en.wikipedia.org/wiki/Joy_Chant',
'http://en.wikipedia.org/wiki/Juanita_Coulson',
'http://en.wikipedia.org/wiki/Judith_Merril',
'http://en.wikipedia.org/wiki/Kate_Elliott',
'http://en.wikipedia.org/wiki/Katharine_Burdekin',
'http://en.wikipedia.org/wiki/Kathleen_Sky',
'http://en.wikipedia.org/wiki/Kit_Reed',
'http://en.wikipedia.org/wiki/Kristine_Kathryn_Rusch',
'http://en.wikipedia.org/wiki/Laura_Antoniou',
'http://en.wikipedia.org/wiki/Lee_Hoffman',
'http://en.wikipedia.org/wiki/Lee_Killough_(author)',
'http://en.wikipedia.org/wiki/Lisa_Ben',
'http://en.wikipedia.org/wiki/Louisa_May_Alcott',
'http://en.wikipedia.org/wiki/Louise_Lawrence',
'http://en.wikipedia.org/wiki/Lynn_Abbey',
'http://en.wikipedia.org/wiki/M._K._Wren',
'http://en.wikipedia.org/wiki/Margaret_St._Clair',
'http://en.wikipedia.org/wiki/Margery_Lawrence',
'http://en.wikipedia.org/wiki/Marie_Corelli',
'http://en.wikipedia.org/wiki/Marijane_Meaker',
'http://en.wikipedia.org/wiki/Marion_Zimmer_Bradley',
'http://en.wikipedia.org/wiki/Marjorie_Bowen',
'http://en.wikipedia.org/wiki/Mary_Moore-Bentley',
'http://en.wikipedia.org/wiki/Mickey_Zucker_Reichert',
'http://en.wikipedia.org/wiki/Nancy_Kilpatrick',
'http://en.wikipedia.org/wiki/Patricia_Matthews',
'http://en.wikipedia.org/wiki/Pauline_Ashwell',
'http://en.wikipedia.org/wiki/Rachel_Cosgrove_Payes',
'http://en.wikipedia.org/wiki/Raphael_Carter',
'http://en.wikipedia.org/wiki/Rebecca_Ore',
'http://en.wikipedia.org/wiki/Rhondi_A._Vilott_Salsitz',
'http://en.wikipedia.org/wiki/Severna_Park_(writer)',
'http://en.wikipedia.org/wiki/Sheri_S._Tepper',
'http://en.wikipedia.org/wiki/Wilmar_H._Shiras'
]
f=open("m2.csv", "wb")

for item in target:

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX dbpedia2: <http://dbpedia.org/property/>
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
            OPTIONAL { ?writer dbpedia2:notableWorks ?notableWorks }
            OPTIONAL { ?writer dbpedia2:period ?period }
            OPTIONAL { ?writer dbpedia2:title ?title }
            OPTIONAL { ?writer dcterms:subject ?subject }
            OPTIONAL { ?writer rdfs:comment ?comment }
            OPTIONAL { ?writer dcterms:subject ?subject }
            OPTIONAL { ?writer owl:sameAs ?sameAs }
            OPTIONAL { ?writer foaf:depiction ?depiction }

        FILTER (LANGMATCHES(LANG(?label), 'en'))
        FILTER (LANGMATCHES(LANG(?comment), 'en'))
        }
        }    
        LIMIT 1
        """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        
        w = csv.DictWriter(f, result.keys())
        w.writeheader()
         
        w.writerow(result)


