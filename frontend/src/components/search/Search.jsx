import { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import axios from 'axios';
import './search.css';
import 'bootstrap'

const API_ENDPOINT = 'http://127.0.0.1:5000'

export default function Search({ searchResult, setSearchResult, searchChoice, setSearchChoice }) {
    const [searchIsLoading, setSearchIsLoading] = useState();
    const [apiResponse, setApiResponse] = useState({});
    const [familyResults, setFamilyResults] = useState({});
    const [familyIsLoading, setFamilyIsLoading] = useState();
    const [narrowIsLoading, setNarrowIsLoading] = useState();
    const [narrowResults, setNarrowResults] = useState({});

    async function api_call(search_type, search_term) {
        const returnData = await axios.post(API_ENDPOINT + "/search?" + "search_type=" + search_type + "&search_string=" + search_term)
            .then(function (response) {
                //console.log(response.data);
                return response.data
            })
            .catch(function (error) {
                console.log(error);
            })
        //console.log(search_type)
        switch (search_type) {
            case "system":
                setApiResponse(returnData);
                setSearchIsLoading(false)
                break;
            case "family":
                setFamilyResults(returnData);
                setFamilyIsLoading(false)
                break;
            case "narrow":
                setNarrowResults(returnData);
                setNarrowIsLoading(false)
                break;
            default:
                break;
        }
    }

    async function api_add(submit_details, submit_type) {
        console.log(submit_details)
        const returnData = await axios.get(API_ENDPOINT + "/db?" + "submit_details=" + submit_details + "&submit_type=" + submit_type)
            .then(function (response) {
                console.log(JSON.parse(response.data.submit_details));
                return response.data
            })
            .catch(function (error) {
                console.log(error);
            })
        //console.log(search_type)
        // switch (search_type) {
        //     case "system":
        //         setApiResponse(returnData);
        //         setSearchIsLoading(false)
        //         break;
        //     case "family":
        //         setFamilyResults(returnData);
        //         setFamilyIsLoading(false)
        //         break;
        //     case "narrow":
        //         setNarrowResults(returnData);
        //         setNarrowIsLoading(false)
        //         break;
        //     default:
        //         break;
        // }
        return returnData
    }

    const handleSubmit = (e) => {
        const search_term = document.getElementById("system_search_term").value
        const search_type = e.target.firstChild.id
        setSearchIsLoading(true)
        api_call(search_type, search_term)
        e.preventDefault();
    }

    const handleNarrow = (e) => {
        const search_type = "narrow"
        const search_term = e.target.id
        setNarrowIsLoading(true)
        api_call(search_type, search_term)
        e.preventDefault();
    }

    const handleSystem = (details) => {
        // console.log(e)
        console.log(details)
        const submit_details = JSON.stringify(details)
        const submit_type = "system"
        // console.log(narrowResults)
        // const search_type = "family"
        // const search_term = e.target.id
        // setFamilyIsLoading(true)
        // setNarrowIsLoading()
        console.log(api_add(submit_details, submit_type))

        event.preventDefault();
    }

    const searchClick = (e) => {
        //console.log(e.target.id)
        setSearchChoice(e.target.id)
    }

    // const searchDisplay = () => {}

    //console.log(searchResult)

    return (
        <>
            <div className="search-menu">
                <ul
                    onClick={searchClick}
                    className="search-menu"
                >
                    <li id="system_search">Search for a system</li>
                    {/* <li id="book_search">Search for a book by title</li> */}
                </ul>
            </div>
            <div>
                {searchChoice == "system_search" ? <SystemSearch searchResult={searchResult} setSearchResult={setSearchResult} handleSubmit={handleSubmit} /> : searchChoice == "book_search" ? <BookSearch handleSearch={handleSubmit} /> : <></>}
            </div>
            {/* TODO: UGLY NESTED TERNARY, need a better option. */}
            {searchIsLoading ? <div className="loading"></div>: searchIsLoading == false ? <SearchResults apiResponse={apiResponse} setApiResponse={setApiResponse} api_call={api_call} familyResults={familyResults} familyIsLoading={familyIsLoading} setFamilyIsLoading={setFamilyIsLoading} handleSystem={handleSystem} narrowIsLoading={narrowIsLoading} narrowResults={narrowResults} searchIsLoading={searchIsLoading} handleNarrow={handleNarrow} /> : <></>}
        </>
    )

}





function SystemSearch({ searchResult, handleSubmit }) {
    return (
        <>
            <form onSubmit={handleSubmit}>
                <label id="system">System Name:
                    <input type="text" id="system_search_term" name="search_term"></input>
                </label>
                <button type="submit">Submit this</button>
            </form>
        </>
    )
}

function BookSearch() {
    return (
        <p>BOOK SEARCH</p>
    )
}

function SearchResults({ apiResponse, searchIsLoading, familyResults, familyIsLoading, setFamilyIsLoading, handleSystem, narrowIsLoading, narrowResults, handleNarrow }) {
    // If there are results, provide them in easy-to-read format.
    // On select, we then want to create the Python object to access details, library, and also create the SQL entry for it.
    const [resultTab, setResultTab] = useState();
    const [showModal, setShowModal] = useState(false);

    // if(searchIsLoading && !familyIsLoading) {
    //     setResultTab("system")
    // }
    // if(!searchIsLoading && familyIsLoading) {
    //     setResultTab("family")
    // }

    var responseTable = []
    if (apiResponse['@total'] === '1') {
        responseTable[0] = apiResponse['item']
    }
    if (apiResponse['@total'] > '1') {
        apiResponse['item'].map((item, i) => {
            responseTable[i] = item;
        })
    }


    return (
        <div className="results-window">
            <div className="system-tab">
                <ul onClick={handleNarrow}>
                    {responseTable.map(item => {
                        return (
                            <li key={item['@id']} id={item['@id']}>{item['name']['@value']}</li>
                        )
                    })}
                </ul>
            </div>
            {narrowIsLoading ? <div className="loading" /> : narrowIsLoading == false ? <div className="narrow-tab"><NarrowTab narrowResults={narrowResults} handleSystem = {handleSystem} /></div> : <></>}
            <div className="family-tab">
                <div className="return-button" onClick={() => setResultTab("system")}>Back</div>
                {familyIsLoading ? <div className="loading" /> : familyIsLoading == false ?
                    <FamilyResults familyResults={familyResults} familyIsLoading={familyIsLoading} setFamilyIsLoading={setFamilyIsLoading} narrowIsLoading={narrowIsLoading} narrowResults={narrowResults} /> : <></>
                }
            </div>
        </div>

    )
}

function NarrowTab({narrowResults, handleSystem}) {
    //console.log(Array.isArray(narrowResults['name']))
    const nameList = {"primary": "",
        "alternates": []
    }
    //console.log(nameList)
    if(Array.isArray(narrowResults['name'])) {
        narrowResults['name'].map((name, i) => {
            //console.log(name)
            if(name['@type'] == "primary") {
                nameList['primary'] = name['@value']
                return
            } else if(name['@type'] == "alternate") {
                nameList['alternates'].push(name['@value'])
            } else {
                return
            }
        })
    } else {
        nameList['primary'] = narrowResults['name']['@value']
    }
    //console.log(nameList['primary'])
    let desc = narrowResults['description'];
    desc = desc.replaceAll("&#10;", "\n");
    const narrowDetails = {
      'name': nameList['primary'],
      'image': narrowResults['image'],
      'desc': desc, //narrowResults['description'],
      'books': narrowResults['link'],
      'id': narrowResults['@id']
    }
    // console.log(narrowDetails)
    return (
        <div>
        <div>
            <p>{narrowDetails['name']}</p>
            <p>{narrowDetails['desc']}</p>
            <p>Number of assets: {narrowDetails['books'].length}</p>
        </div>
        <div>
            <button type="button" className="btn btn-primary" id={narrowDetails['id']} onClick={() => handleSystem(narrowDetails)}>Select this book</button>
        </div>
        <div><button type="button" className="btn btn-danger">Back</button></div>
        </div>
    )
}


function FamilyResults({ familyResults, familyIsLoading, setFamilyIsLoading, narrowIsLoading, narrowResults }) {
    // console.log(JSON.parse(familyResults))
    const familyLibrary = JSON.parse(familyResults)
    // familyResults['library'].map((items, i) =>{
    //         familyLibrary[i] = {
    //         "id": items['@id'],
    //         "title": items['@value']
    //     }})
    //console.log(familyLibrary)


    return (
        <>
            <div>
                {familyLibrary['name']}
            </div>
            <div><img src={familyLibrary['image']} /></div>
            <div className="library-column">
                {familyLibrary['library'].map((items, i) => {
                    return (<div className="library-row" key={i}>
                        <div className="form-check">
  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" />
</div><img src={items['thumbnail']} /><div>{items['bid']}</div><div>{items['name']}</div><div>{items['publisher']}</div><div>{items['series'][0]}</div><div>{items['series'][1]}</div></div>)
                })}
            </div>
        </>
    )
}