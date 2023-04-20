import React, {useState} from 'react';
import { Col, Row, Form, Button, ListGroup } from 'react-bootstrap';

export default function LocalFiles() {
    const [searchFile, setSearchFile] = useState();
    const searchAPI = async (event) => {}


    return(
        <>
            <Form className="mb-3">
                <Form.Group className="mb-3" controlId="fileSearch">
                    <Form.Label className="form-label">Add file to search</Form.Label>
                    <Form.Control type="file" webkitdirectory="" directory="" onChange={searchAPI}/>
                </Form.Group>
            </Form>
            {searchFile ? 
            <Document file={searchFile} /> : <></>}
            </>
    )
}

function Document(props) {
    return (
        <>
        {props.file}
        <Form>
            <Form.Group className="mb-3" controlId="pdfName">
                <Form.Label className="form-label">Document Name</Form.Label>
                <Form.Control name="pdf-name" type="text" value={props.file}></Form.Control>
            </Form.Group>
        </Form>
        </>
    )
}