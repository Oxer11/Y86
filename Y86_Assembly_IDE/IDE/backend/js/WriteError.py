# -*- coding: utf-8 -*-
'''
<tr><td>line1</td>
	<td>Invalid instruction</td>
</tr>
'''

def WriteError(error):
	if len(error)==0:
		return '''<tr><th style="color:green;"><div id="error_state" onclick="fold()">Success!</div><img src="{% static 'IDE/arrowup.png' %}" id="error_arrow"></th>
						</tr>'''
	s='''<tr><th style="color:red;"><div id="error_state" onclick="fold()">Fail!</div><img src="{% static 'IDE/arrowup.png' %}" id="error_arrow"></th>
						</tr>'''
	for key in error.keys():
		s+='''<tr class="error_line"><td>line '''+str(key)+'''</td>
				<td>'''+error[key]+'''</td>
				</tr>'''
	return s