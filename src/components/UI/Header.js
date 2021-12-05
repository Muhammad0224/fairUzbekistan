import styled from "styled-components";
import {Link} from "react-router-dom";
import {Dropdown, DropdownItem, DropdownMenu, DropdownToggle} from "reactstrap";
import {useState} from "react";
import {ReactComponent as Logo} from "../../assets/gerb.svg";

const Header = () => {
    const [toggle, setToggle] = useState(false)
    const [activeLanguage, setActiveLanguage] = useState('UZ')
    const [dropLanguages, setDropLanguage] = useState(['RU', 'EN'])
    const [links, setLinks] = useState([
        {
            name: 'Statistika',
            url: '/statistics'
        },
        {
            name: 'Tezkor aloqa',
            url: '/emergency-call'
        },
        {
            name: 'Ariza yuborish',
            url: '/send-require'
        },
        {
            name: 'Jahon',
            url: '/world'
        },
    ])

    const languages = ['UZ', 'RU', 'EN']

    const changeLanguage = (val) => {
        setActiveLanguage(val);

        setDropLanguage(languages.filter(e => e !== val))
    }

    return (
        <Wrapper>
            <div className="logo-side">
                <div className="logo-wrapper">
                    <Logo/>
                </div>
                <Link to={'/statistics'}>FAIR UZBEKISTAN</Link>
            </div>
            <nav className={'menu'}>
                <ul>
                    {links.map((e,i)=>  <li key={i}>
                        <Link to={e.url}>{e.name}</Link>
                    </li>)}
                </ul>
            </nav>
            <div className="language">
                <Dropdown isOpen={toggle} toggle={() => setToggle(!toggle)}>
                    <DropdownToggle caret className={'dropdown-toggle btn btn-transparent text-light'}>
                        {activeLanguage}
                    </DropdownToggle>
                    <DropdownMenu
                    >
                        {dropLanguages.map((e, i) => <DropdownItem key={i} onClick={() => changeLanguage(e)}>
                            {e}
                        </DropdownItem>)}
                    </DropdownMenu>
                </Dropdown>
            </div>
        </Wrapper>
    )
}

export default Header

const Wrapper = styled.div`
  height: 80px;
  background-color: #020262;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 80px;

  .logo-side {
    display: flex;
    justify-content: center;

    .logo-wrapper {
      width: 60px;

      svg {
        width: 100%;
        height: 100%;
      }
    }

    a {
      text-decoration: none;
      color: #fff;
      font-size: 18px;
      line-height: 80px;
      margin-left: 10px;
    }
  }

  nav {
    height: 100%;
    display: flex;

    ul {
      margin: 0;
      padding: 0;
      list-style: none;
      display: flex;
      align-items: center;
      gap: 15px;

      a {
        color: #fff;
        text-decoration: none;
        padding: 10px;
      }
    }
  }

  .language {
    button:focus {
      box-shadow: none !important;
    }

    .dropdown {
      button {
        background-color: transparent;
        border: none;
      }
    }

    .dropdown-menu {
      min-width: 30px;
    }
  }

`