import { useState, useEffect } from 'react';
import axios from 'axios';

const Metadata = () => {
    const [metadata, setMetadata] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/metadata')
            .then(response => setMetadata(response.data))
            .catch(error => console.error(error));
    }, [metadata]);

    return (
        <div>
            <h2>Face Detection Metadata</h2>
            <ul>
                {metadata.length > 0 && <div style={{ marginBottom: '10px', fontSize: '1.2em', fontWeight: 'bold' }}>
                    Timestamp: {metadata[metadata.length - 1]?.timestamp}, No of faces: {metadata[metadata.length - 1]?.face_count}
                </div>}
            </ul>
        </div>
    );
};

export default Metadata;
