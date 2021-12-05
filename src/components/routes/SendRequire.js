import styled from "styled-components";
import News from "../UI/news/News";
import {Link} from "react-router-dom";

const SendRequire = () => {
    return (
        <Wrapper>
            <div className="left-side">
                <p className={'note'}>**Siz haqingizdagi barcha ma'lumotlar sir saqlanadi</p>
                <form action="" className={'form-control p-3'}>
                    <label htmlFor="">Korrupsiya yuz bergan viloyat nomi</label>
                    <select name="" id="regions" className="form-select">
                        <option value="1"></option>
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
                    <label htmlFor="" className={'mt-3'}>Tuman nomi</label>
                    <select name="" id="regions" className="form-select">
                        <option value="1"></option>
                        <option value="1">Sergeli tumani</option>
                        <option value="1">Yunusobod tumani</option>
                        <option value="1">Olmazor tumani</option>
                        <option value="1">Mirzo-Ulug'bek tumani</option>
                        <option value="1">Chilonzor tumani</option>
                        <option value="1">Yakkasaroy tumani</option>
                        <option value="1">Mirobod tumani</option>
                        <option value="1">Yashnobod tumani</option>
                        <option value="1">Bektemir tumani</option>
                        <option value="1">Uchtepa tumani</option>
                        <option value="1">Shayxontohur tumani</option>
                    </select>
                    <label htmlFor="" className={'mt-3'}>Tashkilot nomi</label>
                    <input type="text" className={'form-control'}/>
                    <label htmlFor="" className={'mt-3'}>Batafsil</label>
                    <textarea className={'form-control'}/>
                    <label htmlFor="" className={'mt-3'}>Emailingizni kiriting</label>
                    <input type={'email'} className={'form-control'}/>
                    <label htmlFor="" className={'mt-3'}>Telefon raqamingizni kiriting</label>
                    <input type={'text'} className={'form-control'}/>

                    <label htmlFor="" className={'mt-3'}>PDF, JPG, MP4</label>
                    <input type={'file'} className={'form-control'}/><br/>

                    <Link to={'/send'}>
                        <button type={'submit'} className={'btn btn-primary mt-3'}>Yuborish</button>
                    </Link>
                </form>
            </div>
            <div className="right-side">
                <p>Yangiliklar</p>
                <News/>
            </div>
        </Wrapper>
    )
}

export default SendRequire

const Wrapper = styled.div`
  padding: 20px 80px;
  display: flex;
  justify-content: space-between;
  gap: 30px;

  .left-side {
    width: 70%;

    .note {
      color: #f00;
    }
  }

  .right-side {
    width: 30%;

    & > p {
      margin: 0 0 0 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid;
      font-size: 18px;
      font-weight: bold;
      color: #25afe7;
    }
  }
`