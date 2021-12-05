import styled from "styled-components";
import {ReactComponent as Logo} from "../../../assets/gerb.svg";
import {ReactComponent as User} from "../../../assets/user.svg";

const ChatRow = ({message}) => {
    return (
        <>
            {message.sender ?
                <Wrapper>
                    <div className="message">
                        <p>{message.text}</p>
                    </div>
                    <div className="icon-wrapper">
                        <User/></div>
                </Wrapper> :
                <Wrapper>
                    <div className="icon-wrapper">
                         <Logo/>
                    </div>
                    <div className="message">
                        <p>{message.text}</p>
                    </div>
                </Wrapper>
            }
        </>

    )
}

export default ChatRow

const Wrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  margin-top: 10px;

  .icon-wrapper {
    width: 30px;
    height: 30px;
    background-color: #ddd;
    border-radius: 50%;

    svg {
      width: 100%;
      height: 100%;
    }
  }

  .message {
    width: 90%;
    padding: 10px;
    background-color: #f1f0f0;
    border-radius: 10px;

    p {
      margin: 0;
      font-size: 14px;
    }
  }
`