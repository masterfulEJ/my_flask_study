- What is best way to embed bokeh in web?

  > Bokeh is a python library for creating interactive plots and figures. With the bokeh server, you can create fully interactive applications with pull-down menus, sliders and other widgets. This has the advantage that you can create fluid and responsive web applications – for example, as you move a slider bar, your plot can respond and update in real-time. However, bokeh plots may only be one part of larger data analysis platform you are trying to build, and once you move beyond a single small application, it can be hard to scale a bokeh server application to accommodate everything you need.
  >
  > 
  >
  > The alternative that I recommend is to use Python flask for your overall web application framework, and then use Bokeh as one component within that framework. This enables complete control over the platform, and also enables you to more easily integrate other components (even other plotting components) and libraries from the larger python data ecosystem. In doing so, you lose some of the built-in fluidity and responsiveness of bokeh server, but you gain maximum flexibility over the entire platform. It’s also much simpler, as the flask framework is very easy to pick up.
