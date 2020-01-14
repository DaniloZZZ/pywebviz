import React from 'react'
import './style.css'

export default Presenter = ({data, setattr}) =>
  {tensor} = data
  if tensor is undefined
    return 'Wait...'
  <div className="torch-presenter">
    Torch tensor:
    <table>
      <tbody>
        { 
            tensor.map (row, i)=>
              if Array.isArray row
                <tr key={i}>
                {
                  row.map (val, j) =>
                    <td key={j}>{val}</td>
                }
                </tr>
              else
                <tr key={i}>{row}</tr>
        }
      </tbody>
    </table>
  </div>
