import {useState, useEffect} from 'react';
//import { api_call } from '../../scripts/api';
import axios from 'axios';

const API_ENDPOINT = 'http://127.0.0.1:5000'

export default function Search({searchResult, setSearchResult, searchChoice, setSearchChoice}) {
    const [searchIsLoading, setSearchIsLoading] = useState();
    const [apiResponse, setApiResponse] = useState({});
    const [familyResults, setFamilyResults] = useState({});
    const [familyIsLoading, setFamilyIsLoading] = useState();
    const [exactIsLoading, setExactIsLoading] = useState();
    const [exactResults, setExactResults] = useState({});

    async function api_call (search_type, search_term) {
        const returnData = await axios.get(API_ENDPOINT + "/search?" + "search_type=" + search_type + "&search_string=" + search_term)
        .then(function (response) {
             console.log(response.data);
            return response.data
         })
         .catch(function (error) {
             console.log(error);
         })
        console.log(search_type)
        switch(search_type) {
            case "system":
                setApiResponse(returnData);
                setSearchIsLoading(false)
                break;
            case "family":
                setFamilyResults(returnData);
                setFamilyIsLoading(false)
                break;
            case "rpgitem":
                setExactResults(returnData);
                setExactIsLoading(returnData)
                break;
            default:
                break;
        }
    }

    const handleSubmit = (e) => {
        const search_term = document.getElementById("system_search_term").value
        const search_type = e.target.firstChild.id
        setSearchIsLoading(true)
        api_call(search_type, search_term)
        e.preventDefault();
      }

    const handleSystem = (e) => {
        const search_type = "family"
        const search_term = e.target.id
        setFamilyIsLoading(true)
        console.log(e.target.id);
        api_call(search_type, search_term)
        e.preventDefault();
    }

    const searchClick = (e) => {
        console.log(e.target.id)
        setSearchChoice(e.target.id)
    }

    // const searchDisplay = () => {}

    console.log(searchResult)

    return(
        <>
        <div>
            <ul 
                onClick={searchClick}
                >
                <li id="system_search">Search for a system</li>
                <li id="book_search">Search for a book by title</li>
            </ul>
        </div>
        <div>
            {searchChoice=="system_search"?<SystemSearch searchResult = {searchResult} setSearchResult={setSearchResult} handleSubmit={handleSubmit} />:searchChoice=="book_search"?<BookSearch handleSearch={handleSubmit} />: <></>}
        </div>
        {/* TODO: UGLY NESTED TERNARY, need a better option. */}
        <div>Your results: {searchIsLoading?"They are loading":searchIsLoading == false?<SearchResults apiResponse = {apiResponse} setApiResponse = {setApiResponse} api_call={api_call} familyResults={familyResults} familyIsLoading={familyIsLoading} setFamilyIsLoading={setFamilyIsLoading} handleSystem={handleSystem} exactIsLoading={exactIsLoading} exactResults={exactResults}/>:<></>}</div>
        </>
    )

}

function SystemSearch({ searchResult, handleSubmit }) {
    return(
        <>
        <p>{searchResult}</p>
        <p>SYSTEM SEARCH</p>
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
    return(
        <p>BOOK SEARCH</p>
    )
}

function SearchResults({apiResponse, familyResults, familyIsLoading, setFamilyIsLoading, handleSystem, exactIsLoading, exactResults}) {
// If there are results, provide them in easy-to-read format.
// On select, we then want to create the Python object to access details, library, and also create the SQL entry for it.


    const responseTable = apiResponse['item'].map((item => {

        return(
                <li key={item['@id']} id={item['@id']}>{item['name']['@value']}</li>
    )}))

    return (
        <>
            <p>TABLE TO BE</p>
            <div>
            <ul onClick={handleSystem}>
            {responseTable}
            </ul>
            </div>
            <div>
            {familyIsLoading?<p>Loading</p>:familyIsLoading == false?
                <FamilyResults familyResults={familyResults} familyIsLoading = {familyIsLoading} setFamilyIsLoading = {setFamilyIsLoading} exactIsLoading={exactIsLoading} exactResults={exactResults} />: <></>
            }
            </div>
        </>
    )
}

function FamilyResults({familyResults,familyIsLoading, setFamilyIsLoading, exactIsLoading, exactResults}) {
    console.log(JSON.parse(familyResults))
    const familyLibrary = []
    familyResults['link'].map((items, i) =>{
        
        if(items['@type'] === "rpg") {
        
            familyLibrary[i] = {
            "id": items['@id'],
            "title": items['@value']
        }}
    })
    console.log(familyLibrary)


    // const family_display = []
    // familyResults.map((item => {
    //     if(item['name'].length >= 1) {
    //         item['name'].map((item_name =>
    //             console.log(item_name)
    //     ))}
    //     // family_display[i] = {
    //     //     "name": 
    //         // }
    //     })
    //     )
            return(
                <>
                 <div>
                     {familyResults['name']['@value']}
                 </div>
                 <div><img src={familyResults['image']}/></div>
                 <div>
                    <ul>
                    {familyResults['link'].map((items, i) =>{
                        return(<li key={i} id={items['@id']}>{items['@value']}</li>)
                    })}
                    </ul>
                 </div>
                </>
            )
}