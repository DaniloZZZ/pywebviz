import React from 'react'
import './style.less'

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
                    <td key={j}>{val.toFixed(3)}</td>
                }
                </tr>
              else
                <tr key={i}>{row}</tr>
        }
      </tbody>
    </table>
  </div>
