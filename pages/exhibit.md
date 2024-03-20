---
title: Exhibit
layout: about
permalink: /exhibit.html
# include CollectionBuilder info at bottom
credits: true
# Edit the markdown on in this file to describe your collection
# Look in _includes/feature for options to easily add features to the page
---

<!---

banner image here
{% include feature/jumbotron.html objectid="https://cdil.lib.uidaho.edu/images/palouse_sm.jpg" %} 

nav menu on top
{% include feature/nav-menu.html sections="Introduction: Women of Carifesta;Lynette Dolphin;Louise Bennett;Lorna Goodison;Guyana Drums;Notes" %}
--> 


<!---experimenting with nav scrollspy on bootstrap-->

<!---
<nav id="navbar-example2" class="navbar bg-body-tertiary px-3 mb-3">
  <a class="navbar-brand" href="#">Navigation</a>
  <ul class="nav nav-pills">
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading1">Introduction: Women of Carifesta</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading2">Lynette Dolphin</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading3">Louise Bennett</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading4">Lorna Goodison</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading5">Guyana Drums</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading6">Notes</a>
    </li>
  </ul>
</nav>
-->

<!---
<div data-bs-spy="scroll" data-bs-target="#navbar-example2" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
  <h2 id="scrollspyHeading1">Introduction: Women of Carifesta</h2>
  <p>...</p>
  <h2 id="scrollspyHeading2">Lynette Dolphin</h2>
  <p>...</p>
  <h2 id="scrollspyHeading3">Louise Bennett</h2>
  <p>...</p>
  <h2 id="scrollspyHeading4">Lorna Goodison</h2>
  <p>...</p>
  <h2 id="scrollspyHeading5">Guyana Drums</h2>
  <p>...</p>
  <h2 id="scrollspyHeading6">Notes</h2>
  <p>...</p>
</div>
-->

<!---
<body>

<nav id="navbar" class="navbar bg-body-tertiary px-3 mb-3">
  <a class="navbar-brand" href="#">Exhibit Navigation</a>
  <ul class="nav nav-pills">
    {% for section in site.sections %}
      <li class="nav-item">
        <a class="nav-link" href="#{{ section.id }}">{{ section.title }}</a>
      </li>
    {% endfor %}
  </ul>
</nav>



<div data-bs-spy="scroll" data-bs-target="#navbar" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
  {% for section in site.sections %}
  <div id="{{ section.id }}">
    {{ section.content | markdownify }}
  </div>
  {% endfor %}
</div>

<!-- Including Bootstrap
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>

</body>
--->

<body data-bs-spy="scroll" data-bs-target="#navbar" data-bs-offset="0" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true">

<nav id="navbar" class="navbar bg-body-tertiary px-3 mb-3">
  <a class="navbar-brand" href="#">Exhibit Navigation</a>
  <ul class="nav nav-pills">
    {% for section in site.sections %}
      <li class="nav-item">
        <a class="nav-link" href="#{{ section.title | slugify }}">{{ section.title }}</a>
      </li>
    {% endfor %}
  </ul>
</nav>

<div class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
  {% for section in site.sections %}
  <div id="{{ section.title | slugify }}">
    <h2>{{ section.title }}</h2>
    {{ section.content | markdownify }}
  </div>
  {% endfor %}
</div>

<!-- Including Bootstrap -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>

</body>



<!---
## Introduction: Women of Carifesta

Chances are that you haven’t heard of the Caribbean Festival of Arts, one of the largest regional festivals of culture in the Caribbean. Starting in Guyana in 1972, the festival has traveled widely around the region over its 50-year history, including editions in Jamaica, Barbados, Cuba, Suriname, and Trinidad & Tobago. As scholars learn more about the history of this festival, it’s becoming clear that it could never have happened without the artistic contributions and organizational work of Caribbean women. Despite prevailing inequalities and bias, women at Carifesta also found opportunities to launch their careers and stage their art in front of thousands. 

This exhibit sheds light on many of those women for the first time, ranging from the first festival in Guyana to the 1981 festival in Barbados. Focusing on these women's work and voices shows how many of the Carifesta events elevated the work of men and heroic masculinity as ideals the region’s people should strive toward, often excluding women in the process. When women were featured, they had stereotypes to contend with–even well-known artists such as Louise Bennett. 

This exhibit displays original historical documents and recordings, offering insights into Carifesta’s past. However, existing Carifesta archives often skew toward that male-centric view. That’s why, along with deep archival research, I’ve conducted interviews with women who were first-hand witnesses and participants in the events of Carifesta. Their memories can go beyond paper traces and bring the festivals to life.

You can start by reading through the individual biographies and stories here. Then, by clicking on each image, you can access more details about the source. The word cloud (under "Subjects"), timeline, and map all provide different ways for you to explore these Carifesta stories.

## Lynette Dolphin

{% include feature/image.html objectid="b01" width="75" caption="Portrait of Lynette Dolphin" %}

In 1966, the Prime Minister of Guyana, Forbes Burnham, delivered a speech to Caribbean artists and writers which has commonly been considered the origin of the Carifesta festival idea. While no women were recorded as attending this meeting, Lynette deWeever Dolphin, Joan Cambridge, Magda Pollard, and Shirley Field-Ridley were crucial to the effort to realize Carifesta ‘72.

The second-ever Guyanese recipient of a scholarship to attend London’s Royal Academy of Music, Lynette Dolphin was an anthologist of Guyanese folk music and an accomplished pianist who performed with the ensemble for the "Legend of Kaieteur," the Guyanese chorale by Philip Pilgrim. For many years, she led the Guyanese National History and Arts Council.

In 1970, Burnham organized a second meeting of Caribbean artists and writers to formulate policy recommendations for the festival. Lynette Dolphin chaired the Music and Dance Sub-Committee. As the official Carifesta Secretariat was assembled, she became Carifesta Director.

{% include feature/image.html objectid="b02" width="75" caption="Lynette Dolphin with Fitzroy Bryant, Minister of Education of St. Kitts and Nevis" %}

In preparation for Carifesta, Dolphin visited numerous Caribbean and Latin American countries, including Suriname, Chile, Peru, and Brazil, persuading governments to send their best artists to Guyana, and asked numerous writers to send contributions to the Carifesta anthology of Caribbean literature.

{% include feature/image.html objectid="b03;b04" width="75" caption="Article on Carifesta diplomatic trips;Brazilian performer gifts Lynette Dolphin flowers at Carifesta finale" %}

One of Dolphin’s most significant trips abroad was to Brazil, where she spent two weeks. The *Ballet Folclórico Viva Bahia*, part of the Brazilian delegation, was one of the most anticipated groups at Carifesta. After touring their new choreography *Odoiá Bahia: A Folk-Pop Spectacle* around Brazil, which included elements of capoeira, candomblé, and samba de roda, the group took their two-hour show to the Carifesta stage. Recognizing Dolphin’s efforts, a member of the group gifted her a bouquet of flowers at the Carifesta closing ceremonies.

{% include feature/image.html objectid="b05;b06" width="75" caption="Lynette Dolphin's Message of support for Carifesta '79 in Cuba;And her statement for Carifesta '76 in Jamaica" %}

Based on the success of Carifesta ‘72, the Cuban government invited Dolphin to Havana to advise on preparations for the 1979 edition of Carifesta. During that festival, Edward Kamau Brathwaite, the Barbadian poet and frequent Carifesta participant, had called her the "MOTHER OF CARIFESTA."[^1]

## Louise Bennett

{% include feature/image.html objectid="c01" width="75" caption="Louise Bennett with Frank Pilgrim" %}

Louise Bennett–the legendary Jamaican storyteller, poet, radio personality, and cultural activist–attended all four Carifesta editions exhibited here. She was given a place of honor at the opening ceremonies of Guyana ’72 and at Cuba ’79 as a leader of the Jamaican delegations. A news article describing her arrival in Guyana, where she met with festival Commissioner Frank Pilgrim in a "V.I.P. lounge," also describes the Olympic Village-style "Festival City," which housed the distinguished visitors. There, the article continues, "specially trained maids have already moved in with their brooms and other paraphenalia [sic] to provide a spic and span welcome."[^2] This contrast between working-class Caribbean women hired to cater to the needs of middle-class performers who are seen as their 'voices', the protectors of lower-class folk traditions, is a poignant reminder of the societal divisions in Guyana and the Caribbean.

{% include feature/image.html objectid="c02" width="75" caption="Bennett on stage for <i>All Kinds of Folk</i>" %}

One of Guyana’s flagship performances during the festival was the variety show "All Kinds of Folk." The show highlighted the diversity of Guyana’s many peoples, descendants from African, Indian, Chinese, and other ethnicities–all of whom were brought there under the duress of enslavement or indentured servitude. Miss Lou’s performance during "All Kinds of Folk" was a hit, inspiring rave reviews in the press.⁠[^3] Her brilliance saved a reportedly "ponderous" and heavy-handed production from "lethargy" and forgettability.⁠[^4]

{% include feature/image.html objectid="c03;c04" width="75" caption="Bennett with her Guyanese counterpart, Auntie Cumsee; " %}

Stealing Guyanese hearts, Louise Bennett appeared during "All Kinds of Folk" with her Guyanese "sister," poet-performer Aunty Cumsee (a.k.a. Pauline Thomas), whom the newspapers called "Guyana’s answer to Jamaica’s Miss Lou." A caption below the picture of the women greeting on stage (see next item)  cites the Jamaican Mento song Auntie Cumsee performed for Miss Lou, "LANG TIME GAL ME NEVAH SEE YOU."⁠ As the original song (usually titled "Dis Long Time, Gal") is about the reunification of old friends or lovers, Cumsee’s homage to Miss Lou infuses this first-time meeting of the two performers with a backstory, as if they had been sisters or best friends all along. One critic even compared this "touching moment" between Thomas and Bennett to a rekindling of "the spirit of the West Indies Federation."⁠[^5] The singer’s invitation to "come mek me hol your han" doubles as a diplomatic handshake

{% include feature/pdf.html objectid="c05" width="75" caption="Barbara Gloudon's 1972 column about Carifesta" %}

Bennett ventured beyond the confines of her V.I.P. housing and the festival venues, taking her performance to the streets and nightclubs of Georgetown. Barbara Gloudon, the Jamaican journalist and playwright—herself a patois pioneer, using it in her newspaper columns—was housed next to Bennett at Echilibar Villas. Miss Lou acted like the consummate celebrity that she was, venturing beyond the barred-off spaces of government officials to mingle with the ordinary people of Guyana. Gloudon’s description highlights the reciprocity of gift-giving between Bennett and her "fans." Her personality transcended languages with laughter. Walking around the market, where she sets so many of her scenes, Bennett brought her "labrishes" to life. Her proximity to these market women echoes the history of marketplaces in plantation societies such as Guyana and Jamaica, where enslaved, and runaway women would work as "higglers" in a state of "provisional freedom within slavery."⁠[^6] In the temporary spaces of spontaneity created during the festival, Bennett became Miss Lou, the authentic embodiment of the people’s voice.

{% include feature/video.html objectid="https://vimeo.com/924805315" width="75" caption="Louise Bennett performing her poem Carifesta Rydim at Carifesta '79 in Cuba" %}

For Carifesta ’79 in Cuba, Bennett was once again a specially honored guest. She had been invited to write and recite new work at the opening ceremony in the national stadium, sharing the stage with Nicolás Guillén, Robin "Dobru" Ravales, and Edward Kamau Brathwaite. Her performance of her new poem, "Carifesta Rydim," was partially captured in Errol Brewster’s film recordings of the Carifesta ’79 opening night.

{% include feature/pdf.html objectid="c07" width="75" caption="The only published version of Carifesta Rydim" %}

Louise Bennett’s verse finds communality in Caribbean rhythm and performance. That much is not surprising for readers of Caribbean poetry. But notice her wordplay on the processes of stirring, blending, turning, shaking, and tempering, and the final punchline of a "ridim" that is "sweet." Her puns blend the techniques of cooking with the devices of poetry (tempering becomes tempo, the rhythmic beat evokes the beating of batter, and turning becomes tune).

## Lorna Goodison

## Guyana Drums

## Notes

[^1]: Edward Kamau Brathwaite, Letter to John La Rose, 4 August 1979. George Padmore Institute, John La Rose Papers.
[^2]: Guyana Graphic. "Louise Bennett Due Tonight." August 22, 1972.
[^3]: Claudette Earle, "Gosh Miss Lou, We Love You!" Sunday Graphic, August 27, 1972.
[^4]: Raschid Osman, "All Kinds of Folk." Sunday Graphic, August 27, 1972.
[^5]: Darryl Dean, "Now a Cultural Federation." Sunday Guardian, September 10, 1972.
[^6]: Shauna Sweeney, "Market Marronage: Fugitive Women and the Internal Marketing System in Jamaica, 1781–1834." The William and Mary Quarterly 76, no. 2 (2019): 197–222, 197.

-->