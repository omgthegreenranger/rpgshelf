import React, {useState} from 'react';
import { Col, Row, Form, Button, ListGroup, ListGroupItem } from 'react-bootstrap';
import axios from 'axios';

export default function LocalFiles() {
    const [searchFile, setSearchFile] = useState();
    const searchAPI = async (event) => {
       setSearchFile("/home/shaggy/Documents/Star Trek/startrekadventures_playersguide.pdf");

       let headersList = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Acess-Control-Allow-Origin": "*"
       }
        
       let bodyContent = JSON.stringify({
            "path": searchFile
       });
        
       let reqOptions = {
            url: "http://127.0.0.1:5000/readfile",
            method: "POST",
            headers: headersList,
            data: bodyContent,
       }
       
       let response = await axios.request(reqOptions);
       console.log(response.data);
    }

    return(
        <>
            <Form className="mb-3">
                <Form.Group className="mb-3" controlId="fileSearch">
                    {/* <Form.Label className="form-label">Add file to search</Form.Label>
                    <Form.Control type="file" onChange={searchAPI}/> */}
                    <Button variant="primary" onClick={searchAPI}>Make the search</Button>
                </Form.Group>
            </Form>
            {/* {searchFile ? 
            <Document file={searchFile} /> : <></>} */}
        {/* <MyFileBrowser /> */}
        </>
    )
}

// function Document(props) {
//     return (
//         <>
//         {props.file}
//         <Form>
//             <Form.Group className="mb-3" controlId="pdfName">
//                 <Form.Label className="form-label">Document Name</Form.Label>
//                 <Form.Control name="pdf-name" type="text" value={props.file}></Form.Control>
//             </Form.Group>
//         </Form>
//         </>
//     )
// }