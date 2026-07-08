import { Filemanager } from "@svar-ui/react-filemanager";
import "@svar-ui/react-filemanager/all.css";
import axios from 'axios';

const API_ENDPOINT = 'http://127.0.0.1:5000'


export default function FileManager() {

    const file_api_call = () => {
        // const returnData = 
        axios.get(API_ENDPOINT + "/readfile")
            .then(function (response) {
                console.log("Response!", response.data);
                // setFilesData(response.data)
                return response.data
            })
            .catch((err) => 
                console.error(err)
            )
    }

    return(
     <div>
     <Filemanager data={JSON.stringify(file_api_call)} />
     <div>HELLO</div>
     </div>
    )
}