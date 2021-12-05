import Header from "./components/UI/Header";
import {Route, Switch} from "react-router-dom";
import Statistics from "./components/routes/Statistics";
import SendRequire from "./components/routes/SendRequire";
import Footer from "./components/UI/Footer";
import EmergencyCall from "./components/routes/EmergencyCall";
import WorldNews from "./components/routes/WorldNews";
import SendForm from "./components/routes/SendForm";

function App(props) {

    return (
        <div>
            <Header/>
            <Switch>
                <Route path={'/statistics'}>
                    <Statistics/>
                </Route>
                <Route path={'/send-require'}>
                    <SendRequire/>
                </Route>

                <Route path={'/emergency-call'}>
                    <EmergencyCall/>
                </Route>
                <Route path={'/world'}>
                    <WorldNews/>
                </Route>
                <Route path={'/send'}>
                    <SendForm/>
                </Route>

                <Route>
                    <Statistics/>
                </Route>

            </Switch>
            <Footer/>
        </div>
    );
}

export default App;
