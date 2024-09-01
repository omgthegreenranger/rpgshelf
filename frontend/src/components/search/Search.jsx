import React, {useState, useEffect} from 'react';
import { InputGroup, Form, Button } from 'react-bootstrap';
//import { api_call } from '../../scripts/api';
import axios from 'axios';

const API_ENDPOINT = 'http://127.0.0.1:5000'

export default function Search({searchResult, setSearchResult, searchChoice, setSearchChoice}) {
    const [searchIsLoading, setSearchIsLoading] = useState();
    const [apiResponse, setApiResponse] = useState({});
    const [familyResults, setFamilyResults] = useState({});
    const [familySearch, setFamilySearch] = useState(false)

    async function api_call (search_type, search_term) {
        const returnData = await axios.get(API_ENDPOINT + "/search?" + "search_type=" + search_type + "&search_string=" + search_term)
        .then(function (response) {
             console.log(response.data);
             setSearchIsLoading(false)
            return response.data
         })
         .catch(function (error) {
             console.log(error);
         })
        console.log(search_type)
        switch(search_type) {
            case "system":
                setApiResponse(returnData);
                break;
            case "family":
                setFamilyResults(returnData);
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
        let search_type = "family"
        let search_term = e.target.id
        console.log(e.target.id);
        api_call(search_type, search_term)
        setFamilySearch(true)
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
        <div>Your results: {searchIsLoading?"They are loading":searchIsLoading == false?<SearchResults apiResponse = {apiResponse} setApiResponse = {setApiResponse} api_call={api_call} familyResults={familyResults} familySearch={familySearch} setFamilySearch={setFamilySearch} handleSystem={handleSystem}/>:<></>}</div>
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

function SearchResults({apiResponse, familyResults, familySearch, setFamilySearch, handleSystem}) {
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
            {familySearch?<div>
                <FamilyResults familyResults={familyResults} familySearch = {familySearch} setFamilySearch = {setFamilySearch} />
            </div>:<></>}
        </>
    )
}

function FamilyResults({familyResults}) {
    console.log(familyResults['name'])
            return(
                <>
                <div>
                    {familyResults['name']['@value']}
                </div>
                <div><img src={familyResults['image']}/> </div>
                </>
            )
}