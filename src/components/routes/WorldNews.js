import styled from "styled-components";
import {ReactComponent as Uzb} from "../../assets/UzbMap.svg";

const WorldNews = () => {
    return (
        <Wrapper>
            <div className="map-uzb mt-3">
                <div className="svg-wrapper">
                    <h3 className={'text-center'}>Viloyatlar kesimida statistika</h3>
                    <Uzb/>
                </div>
                <div className="regions">
                    <h5 className={'text-center'}>Viloyatlar</h5>
                    <table className={'table table-stripped'}>
                        <tbody>
                        <tr>
                            <th>Toshkent shahar</th>
                            <td>309</td>
                        </tr>
                        <tr>
                            <th>Toshkent viloyat</th>
                            <td>326</td>
                        </tr>
                        <tr>
                            <th>Sirdaryo viloyati</th>
                            <td>94</td>
                        </tr>
                        <tr>
                            <th>Jizzax viloyati</th>
                            <td>127</td>
                        </tr>
                        <tr>
                            <th>Samarqand viloyati</th>
                            <td>298</td>
                        </tr>
                        <tr>
                            <th>Navoiy viloyati</th>
                            <td>175</td>
                        </tr>
                        <tr>
                            <th>Buxoro viloyati</th>
                            <td>240</td>
                        </tr>
                        <tr>
                            <th>Qashqadaryo viloyati</th>
                            <td>306</td>
                        </tr>
                        <tr>
                            <th>Surxondaryo viloyati</th>
                            <td>151</td>
                        </tr>
                        <tr>
                            <th>Xorazm viloyati</th>
                            <td>84</td>
                        </tr>
                        <tr>
                            <th>Farg'ona viloyati</th>
                            <td>42</td>
                        </tr>
                        <tr>
                            <th>Andijon viloyati</th>
                            <td>82</td>
                        </tr>
                        <tr>
                            <th>Namangan viloyati</th>
                            <td>37</td>
                        </tr>
                        <tr>
                            <th>Qoraqalpog'iston Respublikasi</th>
                            <td>112</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
                <h3 className={'text-center mt-4'}>Davlatlar kesimida statistika</h3>
                <div className="transparencyEmbed pb-5 " data-year="2020"></div>
        </Wrapper>
    )
}

export default WorldNews

const Wrapper = styled.div`
  height: 800px;

  .map-uzb {
    display: flex;
    justify-content: center;

    .svg-wrapper {
      border: 1px solid #ddd;
      padding: 20px;
    }
    .regions{
      width: 300px;
      background-color: #fff;
      padding: 30px;
    }
  }
`