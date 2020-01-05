import pkg_resources

from delb import Document


def test_custom_loader():
    url = "remote://the_book_of_brian.xml"
    document = Document(url)

    root = document.root
    assert root.local_name == "document"
    assert root["url"] == url


def test_header_properties():
    document = Document("""<?xml version="1.0" encoding="UTF-8"?>
    <document>
        <header>
            <authors>
                <person>
                    <name>
                        <forename>
                            Douglas
                        </forename>
                        <surname>
                            Adams
                        </surname>
                    </name>                    
                </person>
            </authors>
            <title>
                <mainTitle>
                    The Hitchhiker's Guide to the Galaxy
                </mainTitle>
            </title>        
        </header>
        <body/>
    </document>
    """)

    assert document.title == "The Hitchhiker's Guide to the Galaxy"
    assert document.authors == ["Douglas Adams"]


if __name__ == "__main__":
    try:
        pkg_resources.get_distribution("delb-reference-plugins")
    except pkg_resources.DistributionNotFound:
        print(
            "The package that includes the extensions must be installed in order to "
            "use these."
        )
        raise SystemExit(1)

    test_custom_loader()
    test_header_properties()
    print("Everything worked as expected.")
