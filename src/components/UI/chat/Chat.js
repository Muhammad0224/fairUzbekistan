import styled from "styled-components";
import {ReactComponent as Logo} from "../../../assets/gerb.svg";
import {ReactComponent as Send} from "../../../assets/arrow-up.svg";
import ChatRow from "./ChatRow";
import {useState} from "react";

const Chat = () => {
    const [messages, setMessages] = useState([
        {
            sender: false,
            text: 'Sizga qanday yordam berishimiz mumkin'
        },
        {
            sender: true,
            text: 'Salom'
        }
    ])

    const sendMessage = (e) => {
        e.preventDefault()
    }

    return (
        <Wrapper>
            <div className="chat-header">
                <div className="icon-wrapper">
                    <Logo/>
                </div>
                <h6>Korrupsiyaga qarshi kurashish agentligi</h6>
            </div>

            <div className="chat-body">
                {messages.map((e, i) => <ChatRow key={i} message={e}/>)}
            </div>

            <div className="chat-footer">
                <form action="#" className={'form-control'}>
                    <textarea className={'form-control'} placeholder={'Xabar matni...'}/>
                    <button type={'submit'} className={'btn btn-success'} onClick={(e) => sendMessage(e)}><Send/>
                    </button>
                </form>
            </div>
        </Wrapper>
    )
}

export default Chat

const Wrapper = styled.div`
  width: 300px;
  height: 400px;
  position: fixed;
  bottom: 60px;
  z-index: 1;
  right: 40px;
  border-top-left-radius: 10px;
  border-top-right-radius: 30px;
  box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.4);

  .chat-header {
    height: 60px;
    padding: 10px 20px;
    background-color: #404563;
    color: #fff;
    border-top-left-radius: 10px;
    border-top-right-radius: 30px;
    display: flex;
    gap: 10px;

    .icon-wrapper {
      width: 40px;
      height: 40px;

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }

  .chat-body {
    background-color: #fff;
    height: 260px;
    padding: 20px;
  }

  .chat-footer {
    background-color: #fff;
    height: 80px;
    border-top: 1px solid #ddd;


    form {
      display: flex;
      justify-content: space-between;
      border: none;

      textarea {
        border: none;
        resize: none;
      }

      textarea:focus {
        outline: none;
        box-shadow: none;
      }

      button {
        min-width: 30px;
        height: 30px;
        padding: 0;
        border-radius: 50%;
      }
    }
  }
`