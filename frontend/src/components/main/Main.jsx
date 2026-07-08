import {useState} from 'react';
import { Search, Library, Files} from '../index';
// import Button from 'react-bootstrap/';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import './Main.css'

export default function Main() {
    const [searchResult, setSearchResult] = useState([]);
    const [searchChoice, setSearchChoice] = useState();
    const [libraryData, setLibraryData] = useState();
    const [filesData, setFilesData] = useState([])
    return (
        <>
            <div className="component-border main-frame">

                <div><span className="title-letter">L</span><span className="title-word">ibrary</span> <span className="title-letter">O</span><span className="title-word">rganizer</span> <span className="title-word">for</span> <span className="title-letter">R</span><span className="title-word">oleplaying</span> <span className="title-letter">E</span><span className="title-word">nthusiasts</span></div>
                {/* <Search searchResult={searchResult} setSearchResult={setSearchResult} setSearchChoice={setSearchChoice} searchChoice={searchChoice} setLibraryData = {setLibraryData} /> */}
            </div>
            {/* <p>Result = {searchChoice}, {JSON.stringify(searchResult)}</p> */}
            <div>
            <Tabs
                defaultActiveKey="search"
                id="menu-nav"
                className="mb-3"
                >
                <Tab eventKey="search" title="Search">
                    <div>Here is data!</div>
                    </Tab>
                <Tab eventKey="files" title="Files">
            <Files filesData={filesData} setFilesData = {setFilesData} />
                </Tab>
                <Tab eventKey="library" title="Library" disabled >
                    <div>Still more!</div>
                </Tab>
            </Tabs>
            </div>
            <div>
                {/* {libraryData ? <div>This is a library!</div>: <></>}
                <Library setLibraryData = {setLibraryData} libraryData={libraryData}/> */}
            </div>
        </>
    )
}