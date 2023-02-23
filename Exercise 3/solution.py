import re

def logtolist(filename):
  output = [ ]
  ip_address_pattern = re.compile(r'^\d{2}.\d{2,3}.\d{2,3}.\d{2,3}')
  time_stamp_pattern = re.compile(r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})')
  request_pattern = re.compile(r'GET\s([^"]+)')
  for one_line in filename:
    temp_dict = {}
    ip_address = re.match(ip_address_pattern, one_line)
    if ip_address:
      temp_dict['ip_address'] = ip_address.group(0)
    time_stamp = re.search(time_stamp_pattern, one_line)
    if time_stamp:
      temp_dict['time_stamp'] = time_stamp.group(0)
    request = re.search(request_pattern, one_line)
    if request:
      temp_dict['request'] = request.group(0)
    output.append(temp_dict)
  return output


def re_logtolist(filename):
  output = [ ]
  ip_address_pattern = re.compile(r'^\d{2}.\d{2,3}.\d{2,3}.\d{2,3}')
  time_stamp_pattern = re.compile(r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})')
  request_pattern = re.compile(r'GET\s([^"]+)')
  for one_line in filename:
    temp_dict = {}
    ip_address = re.match(ip_address_pattern, one_line)
    if ip_address:
      temp_dict['ip_address'] = ip_address.group(0)
    time_stamp = re.search(time_stamp_pattern, one_line)
    if time_stamp:
      temp_dict['time_stamp'] = time_stamp.group(0)
    request = re.search(request_pattern, one_line)
    if request:
      temp_dict['request'] = request.group(0)
    output.append(temp_dict)
  return output
