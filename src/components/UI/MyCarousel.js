import {Carousel, CarouselControl, CarouselIndicators, CarouselItem} from "reactstrap";
import {useState} from "react";
import styled from "styled-components";
import carousel1 from '../../assets/carousel1_2.jpg'
import bot from '../../assets/bot.jpg'
import carousel3 from '../../assets/carousel3.jpeg'
import {ReactComponent as List} from "../../assets/bar-chart-2.svg";
import {ReactComponent as Check} from "../../assets/check.svg";
import {ReactComponent as Eye} from "../../assets/search.svg";
import {ReactComponent as Play} from "../../assets/send.svg";

const MyCarousel = () => {
    const [activeIndex, setActiveIndex] = useState(0);

    const [animating, setAnimating] = useState(false);

    const items = [
        {
            key: 1,
            src: carousel1,
            data: {
                statistic: [
                    {
                        name: 'Jami holatlar',
                        amount: 1724,
                        icon: <List/>
                    },
                    {
                        name: 'Oldini olinganlar',
                        amount: 1384,
                        icon: <Check/>
                    },
                    {
                        name: 'Ko\'rib chiqilmoqda',
                        amount: 340,
                        icon: <Eye/>
                    }
                ]
            }
        },
        {
            key: 2,
            src: bot,
            data: {
                botIcon: <Play/>,
                botLink: '@fair_uzbekistan_bot'
            }
        },
        {
            key: 3,
            src: carousel3,
            data: {
                text: 'Budjet mablag\'lari tejab qolindi',
                amount: '129 285 000 UZS'
            }
        }
    ];

    const itemLength = items.length - 1

    // Previous button for Carousel
    const previousButton = () => {
        if (animating) return;
        const nextIndex = activeIndex === 0 ?
            itemLength : activeIndex - 1;
        setActiveIndex(nextIndex);
    }

    // Next button for Carousel
    const nextButton = () => {
        if (animating) return;
        const nextIndex = activeIndex === itemLength ?
            0 : activeIndex + 1;
        setActiveIndex(nextIndex);
    }

    const carouselItemData = items.map((item) => {
        return (
            <CarouselItem
                key={item.src}
                onExited={() => setAnimating(false)}
                onExiting={() => setAnimating(true)}
            >
                <img src={item.src} alt={item.altText}/>
                {item.key === 1 &&
                    <div className={'stat-info'}>
                        <div className={'statistics'}>

                            {item.data.statistic.map((e, i) =>
                                <div className={'statistic'}>
                                    <h5 key={i}>
                                        {e.name}
                                    </h5>
                                    <div className="stat-left">
                                        <p>{e.amount}</p>
                                        <div className={'icon-wrapper'}>{e.icon}</div>
                                    </div>
                                </div>
                            )}
                        </div>
                        <button className={'btn btn-info w-100 total'}>UMUMIY STATISTIKA</button>
                    </div>
                }

                {item.key === 2 &&
                    <div className={'bot'}>
                        <div className={'bot-button'}>
                            {item.data.botIcon}
                        </div>
                        <div className="bot-link">
                            {item.data.botLink}
                        </div>
                    </div>
                }

                {item.key === 3 &&
                    <div className={'car-3'}>
                        <p>{item.data.text}</p>
                        <h5>{item.data.amount}</h5>
                    </div>
                }
            </CarouselItem>
        );
    });

    return (
        <Wrapper>
            <Carousel previous={previousButton} next={nextButton}
                      activeIndex={activeIndex}>
                <CarouselIndicators items={items}
                                    activeIndex={activeIndex}
                                    onClickHandler={(newIndex) => {
                                        if (animating) return;
                                        setActiveIndex(newIndex);
                                    }}/>
                {carouselItemData}
                <CarouselControl directionText="Prev"
                                 direction="prev" onClickHandler={previousButton}/>
                <CarouselControl directionText="Next"
                                 direction="next" onClickHandler={nextButton}/>
            </Carousel>
        </Wrapper>
    )
}

export default MyCarousel

const Wrapper = styled.div`
  width: 100%;
  height: 500px;

  img {
    width: 100%;
    height: 500px;
    object-fit: cover;
  }

  .carousel-inner {
    position: relative;

    .stat-info {
      position: absolute;
      width: 350px;
      z-index: 1;
      top: 10%;
      left: 10%;

      .total {
        border-radius: 10px;
        background-color: #020262;
        color: #fff;
        border: 1px solid #020262;
      }

      .statistics {
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);

        .statistic {
          display: flex;
          justify-content: space-between;
          gap: 20px;

          h5, p {
            margin: 0;
            padding: 0;
            text-align: left;
          }

          .stat-left {
            display: flex;
            gap: 5px;
          }

          p {
            font-size: 18px;
          }
        }
      }
    }

    .bot {
      position: absolute;
      top: 40%;
      left: 40%;

      .bot-link {
        width: 250px;
        padding: 0 15px;
        color: #020262;
        font-size: 24px;
        margin: 10px auto;
        border-radius: 10px;
        background-color: #fff;
        text-align: center;
      }

      .bot-button {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background-color: #020262;
        outline: 1px solid #020262;
        animation: btnout 0.7s infinite;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-left: 60px;
      }

      @keyframes btnout {
        0% {
          outline-offset: 0;
        }
        25% {
          outline-offset: 2px;
        }
        50% {
          outline-offset: 5px;
        }

        75% {
          outline-offset: 7px;
        }
        100% {
          outline-offset: 10px;
        }

      }
    }

    .car-3 {
      position: absolute;
      top: 10%;
      right: 15%;
      width: 200px;
      background-color: #020262;
      color: #fff;
      padding: 10px;
      border-radius: 10px;
      font-size: 18px;
      text-align: center;

      h5, p {
        margin: 0;
        padding: 0;
      }
    }
  }
`