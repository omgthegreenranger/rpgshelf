import React, {useState} from 'react';
import { Search, Library } from '../index';
import './Main.css'

export default function Main() {
    const [searchResult, setSearchResult] = useState([]);
    const [searchChoice, setSearchChoice] = useState();
    return (
        <>
            <div className="component-border main-frame">
                <div><span className="title-letter">L</span><span className="title-word">ibrary</span> <span className="title-letter">O</span><span className="title-word">rganizer</span> <span className="title-word">for</span> <span className="title-letter">R</span><span className="title-word">oleplaying</span> <span className="title-letter">E</span><span className="title-word">nthusiasts</span></div>
                <Search searchResult={searchResult} setSearchResult={setSearchResult} setSearchChoice={setSearchChoice} searchChoice={searchChoice} />
            </div>
            <div>
                <Library />
            </div>
            <p>Result = {searchResult}</p>
        </>
    )
}