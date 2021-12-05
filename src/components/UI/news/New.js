import styled from "styled-components";
import {Link} from "react-router-dom";

const New = ({item}) => {
    return (
        <Wrapper>
            <div className="card">
                <img src={item.img} className={'card-img-top'}/>
                <div className="card-body p-3">
                    <h5 className={'card-title'}>{item.title}</h5>
                    <p className={'card-text'}>{item.content}</p>
                    <div className="new-info">
                        <Link to={'/'}>Ko'proq ma'lumot -></Link>
                        <p>{item.date}</p>
                    </div>
                </div>
            </div>
        </Wrapper>
    )
}

export default New

const Wrapper = styled.div`
  .card {
    width: 100%;
    margin-top: 10px;
    border: none;
  }

  .card-body {
    box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.05);

    p {
      font-size: 13px;
    }

    .new-info {
      font-size: 12px;
      display: flex;
      justify-content: space-between;

      p {
        margin: 0;
        color: #999999;
      }

      a {
        color: #999999;
        text-decoration: none;
      }
    }
  }
`