import styled from "styled-components";
import {Link} from "react-router-dom";
import {useState} from "react";

const Footer = () => {
    const [fColor, setFColor] = useState("#020262")
    const [iColor, setIColor] = useState("#020262")
    const [tColor, setTColor] = useState("#020262")

    const facebook = () => {
        return (
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                 stroke={fColor}
                 strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="feather feather-facebook">
                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
            </svg>
        )
    }

    const instagram = () => {
        return (
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                 stroke={iColor}
                 strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="feather feather-instagram">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
        )
    }

    const twitter = () => {
        return (
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                 stroke={tColor}
                 strokeWidth={'2'} strokeLinecap="round" strokeLinejoin="round" className="feather feather-twitter">
                <path
                    d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
            </svg>
        )
    }

    return (
        <Wrapper>
            <div className="top">
                <Link to={'/statistics'}>FAIR UZBEKISTAN</Link>
                <div className="socials">
                    <Link className="social-wrapper" onMouseEnter={() => setFColor("#fff")}
                          onMouseLeave={() => setFColor("#020262")}
                          to={'https://www.facebook.com/antikoruzb/'}>
                        {facebook()}
                    </Link>
                    <Link className="social-wrapper" onMouseEnter={() => setIColor("#fff")}
                          onMouseLeave={() => setIColor("#020262")}
                          to={'/'}>
                        {instagram()}
                    </Link>
                    <Link className="social-wrapper" onMouseEnter={() => setTColor("#fff")}
                          onMouseLeave={() => setTColor("#020262")}
                          to={'https://twitter.com/AntikorUz'}>
                        {twitter()}
                    </Link>
                </div>
            </div>
        </Wrapper>
    )
}

export default Footer

const Wrapper = styled.div`
  height: 60px;
  width: 100%;
  background-color: #020262;
  padding: 0 80px;
  position: fixed;
  bottom: 0;

  .top {
    display: flex;
    justify-content: space-between;
    align-items: center;

    a {
      text-decoration: none;
      color: #fff;
      font-size: 18px;
      line-height: 60px;
      margin-left: 10px;
    }

    .socials {
      margin-right: 30px;
      display: flex;
      gap: 10px;

      .social-wrapper {
        width: 40px;
        height: 40px;
        background-color: #fff;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      .social-wrapper, svg {
        transition: all 0.3s linear;

      }

      .social-wrapper:hover {
        background-color: #020262;

      }
    }
  }
`