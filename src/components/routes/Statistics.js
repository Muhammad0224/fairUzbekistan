import styled from "styled-components";
import MyCarousel from "../UI/MyCarousel";
import {useEffect, useState} from "react";
import {Chart} from "react-google-charts";
import {ReactComponent as Uzb} from "../../assets/UzbMap.svg";

const Statistics = () => {

    const [column, setColumn] = useState({});
    const [lineData, setLineData] = useState({})

    useEffect(() => {
        setColumn({
            old: [
                ['Name', 'Muvaffaqiyatli'],
                ['Toshkent shahar', 250],
                ['Toshkent viloyat', 4200],
                ['Sirdaryo viloyati', 2900],
                ['Jizzax viloyati', 8200],
                ['Samarqand viloyati', 8200],
                ['Navoiy viloyati', 8200],
                ['Buxoro viloyati', 8200],
                ['Qashqadaryo viloyati', 8200],
                ['Surxondaryo viloyati', 8200],
                ['Xorazm viloyati', 8200],
                ['Farg\'ona viloyati', 8200],
                ['Andijon viloyati', 8200],
                ['Namangan viloyati', 8200],
                ['Qoraqalpog\'iston Respublikasi', 8200],
            ],
            new: [
                ['Name', 'Arizalar jami'],
                ['Toshkent shahar', 50],
                ['Toshkent viloyat', 600],
                ['Sirdaryo viloyati', 700],
                ['Jizzax viloyati', 1500],
                ['Samarqand viloyati', 5000],
                ['Navoiy viloyati', 3674],
                ['Buxoro viloyati', 6412],
                ['Qashqadaryo viloyati', 5324],
                ['Surxondaryo viloyati', 3757],
                ['Xorazm viloyati', 6335],
                ['Farg\'ona viloyati', 4587],
                ['Andijon viloyati', 3216],
                    ['Namangan viloyati', 5165],
                ['Qoraqalpog\'iston Respublikasi', 6465],
            ]
        })

        setLineData([
            ['x', 'Muvaffaqiyatli', 'Arizalar soni'],
            ['2019', 35, 59],
            [2020, 24, 46],
            [2021, 20, 31],
        ])
    }, [])

    return (
        <Wrapper className={'clear'}>
            <div className="header">
                <MyCarousel/>
            </div>
            <div className="statistics-content mt-3">
                <form action="" className={'form-control mt-3'}>
                    <label htmlFor="regions">Viloyatlar</label>
                    <select name="" id="regions" className="form-select">
                        <option value="1">Barchasi</option>
                        <option value="1">Toshkent shahar</option>
                        <option value="1">Toshkent viloyat</option>
                        <option value="1">Sirdaryo viloyati</option>
                        <option value="1">Jizzax viloyati</option>
                        <option value="1">Samarqand viloyati</option>
                        <option value="1">Navoiy viloyati</option>
                        <option value="1">Buxoro viloyati</option>
                        <option value="1">Farg'ona viloyati</option>
                        <option value="1">Andijon viloyati</option>
                        <option value="1">Namangan viloyati</option>
                        <option value="1">Surxondaryo viloyati</option>
                        <option value="1">Qashqadaryo viloyati</option>
                        <option value="1">Xorazm viloyati</option>
                        <option value="1">Qoraqalpog'iston Respublikasi</option>
                    </select>

                    <label htmlFor="directions" className={'mt-3'}>Yo'nalishlar</label>
                    <select name="" id="directions" className="form-select">
                        <option value="1">Barchasi</option>
                        <option value="1">Iqtisodiyot</option>
                        <option value="1">Qishloq xo'jaligi</option>
                        <option value="1">Boshqaruv Hokimiyati</option>
                        <option value="1">Bank</option>
                    </select>
                </form>
                <div className="charts mt-3">
                    <Chart
                        width={'600px'}
                        height={'300px'}
                        chartType="ColumnChart"
                        loader={<div>Loading Chart</div>}
                        diffdata={column}
                        options={{
                            legend: {position: 'top'},
                        }}
                        rootProps={{'column-testid': '4'}}
                    />
                    <Chart
                        width={'600px'}
                        height={'300px'}
                        chartType="LineChart"
                        loader={<div>Loading Chart</div>}
                        data={lineData}
                        options={{
                            hAxis: {
                                title: 'Yillar',
                            },
                            vAxis: {
                                title: 'Toshkent',
                            },
                            series: {
                                1: {curveType: 'function'},
                            },
                        }}
                        rootProps={{'data-testid': '2'}}
                    />
                </div>
            </div>

        </Wrapper>
    )
}

export default Statistics

const Wrapper = styled.div`
  .header {
    height: 500px;
  }

  .statistics-content {
    height: 200px;
    padding: 10px 80px;

    form {
      padding: 20px 10px;
    }

    .charts {
      display: flex;
      justify-content: space-between;
      gap: 30px;
      height: 500px;
    }

  }
`