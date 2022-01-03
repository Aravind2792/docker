{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c5f38f13",
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly \n",
    "import dash \n",
    "from dash import html\n",
    "from dash import dcc\n",
    "from plotly import graph_objs as go\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "93d235ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_excel('Alathiyur CM1 data.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2128f44f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>DAY</th>\n",
       "      <th>Feed</th>\n",
       "      <th>DP</th>\n",
       "      <th>MKW</th>\n",
       "      <th>SepSpeed</th>\n",
       "      <th>I/Ldraft</th>\n",
       "      <th>I/LTemp</th>\n",
       "      <th>O/LTemp</th>\n",
       "      <th>MFanSpeed</th>\n",
       "      <th>RejectTPH</th>\n",
       "      <th>ActualBlaine</th>\n",
       "      <th>Predicted Blaine</th>\n",
       "      <th>R-Square</th>\n",
       "      <th>Mill Run Status</th>\n",
       "      <th>Error</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-05-15 14:13:14</td>\n",
       "      <td>154.42</td>\n",
       "      <td>355.77</td>\n",
       "      <td>2224.73</td>\n",
       "      <td>67.76</td>\n",
       "      <td>34.52</td>\n",
       "      <td>143.82</td>\n",
       "      <td>97.63</td>\n",
       "      <td>926.03</td>\n",
       "      <td>16.17</td>\n",
       "      <td>351</td>\n",
       "      <td>361.11</td>\n",
       "      <td>0.26</td>\n",
       "      <td>1</td>\n",
       "      <td>10.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-05-15 14:13:34</td>\n",
       "      <td>152.71</td>\n",
       "      <td>355.43</td>\n",
       "      <td>2224.40</td>\n",
       "      <td>67.79</td>\n",
       "      <td>35.60</td>\n",
       "      <td>143.82</td>\n",
       "      <td>97.63</td>\n",
       "      <td>927.25</td>\n",
       "      <td>16.19</td>\n",
       "      <td>351</td>\n",
       "      <td>361.11</td>\n",
       "      <td>0.26</td>\n",
       "      <td>1</td>\n",
       "      <td>10.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-05-15 14:13:54</td>\n",
       "      <td>152.16</td>\n",
       "      <td>355.07</td>\n",
       "      <td>2221.69</td>\n",
       "      <td>67.79</td>\n",
       "      <td>36.13</td>\n",
       "      <td>143.82</td>\n",
       "      <td>97.60</td>\n",
       "      <td>926.51</td>\n",
       "      <td>16.22</td>\n",
       "      <td>351</td>\n",
       "      <td>361.11</td>\n",
       "      <td>0.26</td>\n",
       "      <td>1</td>\n",
       "      <td>10.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-05-15 14:14:14</td>\n",
       "      <td>154.95</td>\n",
       "      <td>354.53</td>\n",
       "      <td>2215.45</td>\n",
       "      <td>67.84</td>\n",
       "      <td>37.11</td>\n",
       "      <td>143.82</td>\n",
       "      <td>97.67</td>\n",
       "      <td>927.25</td>\n",
       "      <td>14.56</td>\n",
       "      <td>351</td>\n",
       "      <td>361.11</td>\n",
       "      <td>0.26</td>\n",
       "      <td>1</td>\n",
       "      <td>10.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-05-15 14:14:34</td>\n",
       "      <td>156.64</td>\n",
       "      <td>354.17</td>\n",
       "      <td>2178.54</td>\n",
       "      <td>67.79</td>\n",
       "      <td>36.13</td>\n",
       "      <td>143.82</td>\n",
       "      <td>97.71</td>\n",
       "      <td>926.03</td>\n",
       "      <td>15.39</td>\n",
       "      <td>351</td>\n",
       "      <td>361.11</td>\n",
       "      <td>0.26</td>\n",
       "      <td>1</td>\n",
       "      <td>10.11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  DAY    Feed      DP      MKW  SepSpeed  I/Ldraft  I/LTemp  \\\n",
       "0 2021-05-15 14:13:14  154.42  355.77  2224.73     67.76     34.52   143.82   \n",
       "1 2021-05-15 14:13:34  152.71  355.43  2224.40     67.79     35.60   143.82   \n",
       "2 2021-05-15 14:13:54  152.16  355.07  2221.69     67.79     36.13   143.82   \n",
       "3 2021-05-15 14:14:14  154.95  354.53  2215.45     67.84     37.11   143.82   \n",
       "4 2021-05-15 14:14:34  156.64  354.17  2178.54     67.79     36.13   143.82   \n",
       "\n",
       "   O/LTemp  MFanSpeed  RejectTPH  ActualBlaine  Predicted Blaine  R-Square  \\\n",
       "0    97.63     926.03      16.17           351            361.11      0.26   \n",
       "1    97.63     927.25      16.19           351            361.11      0.26   \n",
       "2    97.60     926.51      16.22           351            361.11      0.26   \n",
       "3    97.67     927.25      14.56           351            361.11      0.26   \n",
       "4    97.71     926.03      15.39           351            361.11      0.26   \n",
       "\n",
       "   Mill Run Status  Error   \n",
       "0                1   10.11  \n",
       "1                1   10.11  \n",
       "2                1   10.11  \n",
       "3                1   10.11  \n",
       "4                1   10.11  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "df206d99",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=dash.Dash()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6b4a8077",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 41745 entries, 0 to 41744\n",
      "Data columns (total 15 columns):\n",
      " #   Column            Non-Null Count  Dtype         \n",
      "---  ------            --------------  -----         \n",
      " 0   DAY               41745 non-null  datetime64[ns]\n",
      " 1   Feed              41745 non-null  float64       \n",
      " 2   DP                41745 non-null  float64       \n",
      " 3   MKW               41745 non-null  float64       \n",
      " 4   SepSpeed          41745 non-null  float64       \n",
      " 5   I/Ldraft          41745 non-null  float64       \n",
      " 6   I/LTemp           41745 non-null  float64       \n",
      " 7   O/LTemp           41745 non-null  float64       \n",
      " 8   MFanSpeed         41745 non-null  float64       \n",
      " 9   RejectTPH         41745 non-null  float64       \n",
      " 10  ActualBlaine      41745 non-null  int64         \n",
      " 11  Predicted Blaine  41745 non-null  float64       \n",
      " 12  R-Square          41745 non-null  float64       \n",
      " 13  Mill Run Status   41745 non-null  int64         \n",
      " 14  Error             41745 non-null  float64       \n",
      "dtypes: datetime64[ns](1), float64(12), int64(2)\n",
      "memory usage: 4.8 MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e8e47a8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "app.layout=html.Div([\n",
    "    dcc.Graph(id=\"Test_plot\",\n",
    "             figure={\n",
    "                 'data':[go.Scatter(x=df['Feed'],y=df['DP'],mode=\"markers\")],\n",
    "                 'layout':go.Layout(title=\"Test plot\",xaxis={'title':\"Feed\"},yaxis={'title':'DP'},hovermode='closest')\n",
    "                    }\n",
    "             )\n",
    "           ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ca1fd1fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/deps/react@16.v2_0_0m1638426371.14.0.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/deps/prop-types@15.v2_0_0m1638426371.7.2.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/deps/polyfill@7.v2_0_0m1638426371.12.1.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/deps/react-dom@16.v2_0_0m1638426371.14.0.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/dash_table/bundle.v5_0_0m1638426371.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/html/dash_html_components.v2_0_0m1638426371.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/dcc/dash_core_components-shared.v2_0_0m1638426371.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/dash-renderer/build/dash_renderer.v2_0_0m1638426371.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/dcc/dash_core_components.v2_0_0m1638426371.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-dependencies HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_favicon.ico?v=2.0.0 HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-layout HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/dcc/async-graph.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2021 12:34:36] \"GET /_dash-component-suites/dash/dcc/async-plotlyjs.js HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d563fbf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
