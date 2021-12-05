import styled from "styled-components";
import PDF from '../../assets/ARIZA_T.pdf'

const SendForm = () => {
    return (
        <Wrapper>
            <p className={'alert-success p-3 mb-3'}>Arizangiz muvaffaqiyatli yuborildi</p>

            <embed src={PDF} width="100%" height="700" type="application/pdf"/>
            <p className={'alert-success p-3 alert-bottom'}>Kiritilgan fayllar o'rganib chiqilishi uchun mutaxasislarga jo'natildi</p>
        </Wrapper>
    )
}

export default SendForm

const Wrapper = styled.div`
  padding: 10px 80px;
  overflow-x: hidden;

  p {
    margin: 0;
  }
  
  .alert-bottom{
    margin-bottom: 100px;
  }

  .pdf-template {
    width: 70%;
    margin: 0 auto 100px ;
    padding: 50px 0;
    border: 1px solid gray;
    box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
    background-color: #fff;
    
    .pdf-header {
      width: 100%;
      margin: 10px 10px 10px 65%;
      font-size: 18px;
    }

    .text-center {
      font-size: 18px;
      font-weight: bold;
      margin: 15px;
    }

    .pdf-body {
      padding: 0 30px;
    }
    
    .info{
      width: 70%;
      margin: 0 auto;
      font-weight: bold;
      
      .info-row{
        display: flex;
        justify-content: space-between;
        gap: 250px;
      }
    }
  }
`