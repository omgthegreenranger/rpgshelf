import React, {useState} from 'react';

import { Search, Library } from '../index';

export default function Main() {
    const [searchResult, setSearchResult] = useState([]);
    const [searchChoice, setSearchChoice] = useState();
    return (
        <>
            <div>
                <div>This is the Main component</div>
                <Search searchResult={searchResult} setSearchResult={setSearchResult} setSearchChoice={setSearchChoice} searchChoice={searchChoice} />
            </div>
            <div>
                <Library />
            </div>
            <p>Result = {searchResult}</p>
        </>
    )
}