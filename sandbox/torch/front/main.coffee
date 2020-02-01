import React from 'react'
import Tensor from './tensor.coffee'
import './style.less'
import LeClient from 'legimens'


export default ModelPresenter = ({data, setattr, addr}) =>
  {model} = data

  if model is undefined
    return 'Wait...'

  console.log 'model', model

  <div style={{width:'100%',height:'100%', overflow: 'auto'}} className="torch-model-presenter">
    Torch model:
      {JSON.stringify model}
    <div>
        {
          model.value.map (item, idx) =>
            <div>
              <p> {item[0]} </p>
              <LeClient addr={addr} refval={item[1]}>
              {
                (variable, setattr)->
                  console.log 'data', variable, setattr
                  if not variable
                    return 'Loading'
                  <div className='container'>
                    <Tensor data={variable}/>
                  </div>
              }
              </LeClient>
            </div>
        }
    </div>
  </div>
