function makeTimeStamp(dateString)
    local pattern = "(%d+)%-(%d+)%-(%d+)"
    local xyear, xmonth, xday = dateString:match(pattern)
    local convertedTimestamp = os.time({year = xyear, month = xmonth, 
        day = xday})
    return convertedTimestamp
end

function Meta(m)
  m.date = os.date('%Y-%m-%d %H:%M:%S', makeTimeStamp(m.date))
  return m
end
