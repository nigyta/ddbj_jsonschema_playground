// import { RJSFSchema } from '@rjsf/utils';
import validator from '@rjsf/validator-ajv8';
// import Form from '@rjsf/core';
import Form from '@rjsf/bootstrap-4';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.min.css';

// for debugging
// const schema: RJSFSchema = {
//   title: 'Todo',
//   type: 'object',
//   required: ['title'],
//   properties: {
//     title: { type: 'string', title: 'Title', default: 'A new task' },
//     done: { type: 'boolean', title: 'Done?', default: false },
//   },
// };


const log = (type) => console.log.bind(console, type);

function App() {

  const [schemaName, setSchemaName] = useState("reference");
  const [schemaTypes, setSchemaTypes] = useState(null);
  const [schema, setSchema] = useState(null);

  useEffect(() => {
    // schemaの一覧を取得
    axios.get('http://localhost:8000/get_schema_types',{
      params: {_: new Date().getTime()}
    })
      .then(response => setSchemaTypes(response.data)) // レスポンスからデータを取得してセット
      .catch(error => console.error('Error fetching data:', error));
  }, []); // 空の依存配列でエフェクトを一度だけ実行


  useEffect(() => {
    // jsonschema 取得
    console.log("Schema Selected:", schemaName)
    axios.post('http://localhost:8000/schema',{name: schemaName})
      .then((response) => {console.log("fetched");setSchema(response.data)}) // レスポンスからデータを取得してセット
      .catch(error => console.error('Error fetching data:', error));
    console.log(schema);
  }, [schemaName]);


  const on_schema_type_change = (e) => {
    // console.log(e.formData.name);
    setSchemaName(e.formData.name);
  }

  return (
    <div className="App container">
    {schemaTypes ?
      <Form schema={schemaTypes} validator={validator} onChange={on_schema_type_change}>
      </Form>
    :
      <p>loading...</p>
    }

    <hr/><br/><br/>

    {schema ?
      <Form
          schema={schema}
          validator={validator}
          onChange={log('changed')}
          onSubmit={log('submitted')}
          onError={log('errors')}
      >
      </Form>
    :
      <p>loading...</p>
    }
    </div>
  );
}

export default App;
