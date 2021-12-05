import styled from "styled-components";
import Chat from "../UI/chat/Chat";
import {Link} from "react-router-dom";
import {useState} from "react";
import {ReactComponent as Phone} from "../../assets/phone-call.svg";
import {ReactComponent as Browser} from "../../assets/globe.svg";
import {ReactComponent as Mail} from "../../assets/mail.svg";
import {ReactComponent as Telegram} from "../../assets/send (1).svg";

const EmergencyCall = () => {


    return (
        <Wrapper>
            <div className="contact">
                <div className="details">
                    <div className="detail-row mb-3">
                        <Phone/>
                        <p className="fw-bold">Telefon:</p>
                        <p>(998 71) 202 04 02 (431)</p>
                    </div>
                    <div className="detail-row">
                        <Phone/>
                        <p className="fw-bold">Call center:</p>
                        <p>7777</p>
                    </div>
                    <div className="detail-row mt-3">
                        <Browser/>
                        <p className="fw-bold my-2">Sayt:</p>
                        <Link to={'/'}>www.anticorruption.uz</Link>
                    </div>

                    <div className="detail-row mt-3">
                        <Mail/>
                        <p className="fw-bold my-2">Pochta:</p>
                        <Link>antikor@exat.uz</Link>
                    </div>


                    <div className="detail-row mt-3">
                        <Telegram/>
                        <p className="fw-bold my-2">Telegram:</p>
                        <Link to={'https://t.me/fair_uzbekistan_bot'}>@fair_uzbekistan_bot</Link>
                    </div>

                </div>
                <div className="map">
                    <iframe
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2997.6332047318397!2d69.26376911492409!3d41.29508670967582!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38ae8add3163ba25%3A0x35880c86f33bd532!2zOCDRg9C70LjRhtCwINCo0L7RgtCwINCg0YPRgdGC0LDQstC10LvQuCwg0KLQsNGI0LrQtdC90YIgMTAwMDcwLCDQo9C30LHQtdC60LjRgdGC0LDQvQ!5e0!3m2!1sru!2s!4v1638535197535!5m2!1sru!2s"
                        width="600" height="400" allowFullScreen="" loading="lazy"></iframe>
                </div>
            </div>
            <Chat/>
        </Wrapper>

    )
}

export default EmergencyCall

const Wrapper = styled.div`
  padding: 10px 80px;

  .contact {
    width: 80%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.4);

    .details {
      width: 500px;
      padding: 20px;

      .detail-row {
        display: flex;
        align-items: center;
        gap: 10px;

        p {
          margin: 0;
        }

        a {
          display: block;

        }
      }
    }
  }

`