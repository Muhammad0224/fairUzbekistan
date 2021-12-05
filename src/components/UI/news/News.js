import styled from "styled-components";
import {useState} from "react";
import New from "./New";
import new1 from '../../../assets/news1.jpg'
import new2 from '../../../assets/news2.jpg'
import new3 from '../../../assets/news3.jpg'

const News = () => {
    const [news, setNews] = useState([
        {
            id: 1,
            img: new1,
            title: 'KORRUPSIYAGA QARSHI KURASHISH VA OCHIQLIK BO‘YICHA TOSHKENT FORUMI',
            content: 'Joriy yilning 3 dekabr kuni poytaxtimizdagi "Hillton" mehmonxonasida “Korrupsiyaga qarshi kurashish va ochiqlik bo‘yicha Toshkent forumi” bo‘lib o‘tdi.',
            date: '03/12/2021'
        },
        {
            id: 2,
            img: new2,
            title: 'OLIY MAJLIS QONUNCHILIK PALATASINING NAVBATDAGI SESSIYASI OAV ORQALI JONLI EFIRDA NAMOYISH ETILDI',
            content: 'Korrupsiyaga qarshi kurashish agentligi tomonidan O‘zbekiston Respublikasi Prezidentining 2021 yilning 16 iyundagi...',
            date: '03/12/2021'
        },
        {
            id: 3,
            img: new3,
            title: 'XALQARO PRESS KLUB: "O‘ZBEKISTONDA AKSILKORRUPSIYAVIY ISLOHOTLAR, MAVJUD MUAMMOLAR VA ISTIQBOLDAGI REJALAR" ',
            content: 'Bugun Xalqaro press-klubning "O‘zbekistonda aksilkorrupsiyaviy islohotlar, mavjud muammolar va istiqboldagi rejalar" mavzusidagi navbatdagi sessiyasi bo‘lib o‘tdi. ',
            date: '02/12/2021'
        }
    ])

    return (
        <Wrapper>
            {news.map((e, i) => <New key={i} item={e}/>)}
        </Wrapper>
    )
}

export default News

const Wrapper = styled.div`
  padding: 10px 20px;

`