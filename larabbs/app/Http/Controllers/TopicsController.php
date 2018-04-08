<?php

namespace App\Http\Controllers;

use App\Models\Topic;
use App\Http\Requests\TopicRequest;
use Illuminate\Http\Request;

/**
 * Class TopicsController
 *
 * @package App\Http\Controllers
 */
class TopicsController extends Controller
{
    /**
     * TopicsController constructor.
     */
    public function __construct()
    {
        $this->middleware('auth', ['except' => ['index', 'show']]);
    }

    public function index(Request $request, Topic $topic)
	{
		$topics = $topic->withOrder($request->order)->paginate(20);
		return view('topics.index', compact('topics'));
	}

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function show(Topic $topic)
    {
        return view('topics.show', compact('topic'));
    }

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */public function create(Topic $topic)
	{
		return view('topics.create_and_edit', compact('topic'));
	}

    /**
     * @param \App\Http\Requests\TopicRequest $request
     *
     * @return \Illuminate\Http\RedirectResponse
     */public function store(TopicRequest $request)
	{
		$topic = Topic::create($request->all());
		return redirect()->route('topics.show', $topic->id)->with('message', 'Created successfully.');
	}

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */public function edit(Topic $topic)
	{
        $this->authorize('update', $topic);
		return view('topics.create_and_edit', compact('topic'));
	}

    /**
     * @param \App\Http\Requests\TopicRequest $request
     * @param \App\Models\Topic               $topic
     *
     * @return \Illuminate\Http\RedirectResponse
     */public function update(TopicRequest $request, Topic $topic)
	{
		$this->authorize('update', $topic);
		$topic->update($request->all());

		return redirect()->route('topics.show', $topic->id)->with('message', 'Updated successfully.');
	}

    /**
     * @param \App\Models\Topic $topic
     *
     * @return \Illuminate\Http\RedirectResponse
     */public function destroy(Topic $topic)
	{
		$this->authorize('destroy', $topic);
		$topic->delete();

		return redirect()->route('topics.index')->with('message', 'Deleted successfully.');
	}
}
