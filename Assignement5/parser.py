import re

def parse_nwodkram(regex):
	"""
	Function for text conversion from nwodkram syntax to HTML.

	Takes string argument only!
	"""

	# The name regex is somewhat missleading here. It should be
	# output_text or such

	regex = re.sub(r"<(?!a href)(.+?)>\(w=(\d+?),h=(\d+?)\)", "<img src=\"%s\" style=\"width:%spx;height:%spx\";>" % (r"\1", r"\2", r"\3"), regex)
	regex = re.sub(r"\[wp:(.*?)\]", "<a href=\"www.wikipedia.org/wiki/%s\">Search Wikipedia for %s</a>" % (r"\1", r"\1"), regex)
	regex = re.sub(r"\[(.+?)\]\((.*?)\)", r"<a href='http://\2'>\1</a>", regex)
	regex = re.sub(r"http://http", r"http", regex)
	regex = re.sub(r"(?<!\\)\*(.*?(?<!\\))\*", r"<i>\1</i>", regex)
	regex = re.sub(r"(?<!\\)\%(.*?(?<!\\))\%", r"<b>\1</b>", regex)

	regex = re.sub(r"\>\>(.*)", r"<blockquote>\1</blockquote>", regex)
	regex = re.sub(r"\\\%", r"%", regex)
	regex = re.sub(r"\\\*", r"*", regex)
	return regex

if __name__ == "__main__":

	inputtext = """
	%Lorem% ipsum *dolor sit amet*, consectetur *adipiscing elit. Nullam tempor* nunc at justo tincidunt congue. %Aliquam hendrerit mollis pretium! Praesent id% mi est. [Praesent,](www.praesent.com) sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

	>>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla *eget eros euismod volutpat. Suspendisse* id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat %molestie \*libero vel\%\% pulvinar? Sed% a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.

	Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in \%% urna. \% Fusce% in *sapien %mau\*ris.% Duis purus dui*, viverra in tellus eu, imperdiet fringilla [felis. Curabitur rhoncus tincidunt varius. Cras](inf3331.no) gravida metus ut [wp:vestibulum] vestibulum. \*Integer cursus* ex\* in rutrum volutpat*. Nunc scelerisque gravida risus sed ullamcorper. Proin [lorem,](https://www.malesuada.com) massa <https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif>(w=100,h=40) quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio *bibendum.*
	"""
	outputtext = """
	<b>Lorem</b> ipsum <i>dolor sit amet</i>, consectetur <i>adipiscing elit. Nullam tempor</i> nunc at justo tincidunt congue. <b>Aliquam hendrerit mollis pretium! Praesent id</b> mi est. <a href='http://www.praesent.com'>Praesent,</a> sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

	<blockquote>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla <i>eget eros euismod volutpat. Suspendisse</i> id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat <b>molestie *libero vel%% pulvinar? Sed</b> a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.</blockquote>

	Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in %<b> urna. % Fusce</b> in <i>sapien <b>mau*ris.</b> Duis purus dui</i>, viverra in tellus eu, imperdiet fringilla <a href='http://inf3331.no'>felis. Curabitur rhoncus tincidunt varius. Cras</a> gravida metus ut <a href="www.wikipedia.org/wiki/vestibulum">Search Wikipedia for vestibulum</a> vestibulum. *Integer cursus<i> ex* in rutrum volutpat</i>. Nunc scelerisque gravida risus sed ullamcorper. Proin <a href='https://www.malesuada.com'>lorem,</a> massa <img src="https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif" style="width:100px;height:40px";> quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio <i>bibendum.</i>
	"""
	# simple test to check input and outputtext
	if (parse_nwodkram(inputtext) == outputtext):
		print("\n parser returned the same as outputtext!")
	else:
		import difflib
		for i,s in enumerate(difflib.ndiff(parse_nwodkram(inputtext), outputtext)):
			if s[0]==' ': continue
			elif s[0]=='-':
				print(u'Delete "{}" from position {}'.format(s[-1],i))
			elif s[0]=='+':
				print(u'Add "{}" to position {}'.format(s[-1],i))
